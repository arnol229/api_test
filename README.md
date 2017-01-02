API Technical Test
------------------

This site is provides two API endpoints, /api/threat/ip/<IP_ADDRESS> & /api/traffic

The IP Details API utilizes alienvaults reputation API to gather and relay statistics

The traffic API displays recorded user's and their querys against the Details API


============
Installation
============
Packaged in this repo is a docker friendly script that will pull the latest code and spin up a container. 

If you would rather use the built in django function, then install the REQUIREMENTS.txt with pip and use python manage.py runserver to serve locally.

=====================
Application Structure
=====================

All valid path requests fall through an api_response decorator function.
The decorator will standardizes calls by applying an order of operations:
1. load or create the users profile onto the request object
2. run api function
3. create failure/success response objects if GET param 'format' has been passed
4. create visit record
5. Return response


The app is broken into 2 modules: api and datastore.

1. Datastore was intended to host all data querying (internal or proxy). For whatever reason, Django stopped recognizing the datastore app (v1.9 related?).
I moved the django models inside of the api module and continued from there.

2. The api module houses the class based views that are routed from the base urls file. The settings.py file houses the URL routes for proxy calls that need to be made to retrieve IP details.