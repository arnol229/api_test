import logging
from functools import wraps
from rest_framework.response import Response
import datetime

from api_test.api.models import User, Visit
from rest_framework.decorators import api_view


def error_response(message=None):
    """Base response for all errors."""
    return {
        'success': False,
        'message': message
    }


def success_response(result=None):
    """Base response for all successes."""
    return {
        'success': True,
        'result': result
    }


def api_response(f):
    """
    API wrapper
    1. get user id through cookie or create_with_id
    2. run api function
    3. create failure/success response object
    4. create visit record
    """

    @wraps(f)
    @api_view(['GET'])
    def wrapper(*args, **kwargs):
        wrapped = True
        request = args[0]

        try:
            user_id = request.COOKIES.get("AlienVaultID", None)
            if not user_id:
                request.user = User.create_with_id()
                logging.info("User_Created:{0}".format(request.user.alienvault_id))
            else:
                request.user = User.objects.get(alienvault_id=user_id)

            # Run the API function
            response = f(*args, **kwargs)
            response_obj = success_response(response.data)
            response_code = 200

        except Exception as e:
            response_obj = error_response(message=str(e))
            response_code = 500
            logging.exception(e)

        Visit.objects.create(
            user=request.user,
            address=request.META.get('REMOTE_ADDR', 'Unknown'),
            endpoint=request.path,
            result=response_obj['success']
        )

        #constructing another Response object to get a structured response...
        if request.GET.get('format'):
            response = Response(response_obj,
                                status=response_code)

        if not 'AlienVaultID' in request.COOKIES:
            # Set cookie to expire in 1 year
            max_age = 365 * 24 * 60 * 60
            expires = datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age)
            response.set_cookie(
                'AlienVaultID',
                request.user.alienvault_id,
                expires=expires.utctimetuple(),
                max_age=max_age)

        return response

    return wrapper
