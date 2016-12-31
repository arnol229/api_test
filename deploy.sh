!#bash
printf "\n\n\n\e[32m-- Alien Vault API Service --\e[0m\n\n\n"
sleep 1

printf "\e[32mUpdating \e[0m\n\n\n"
sleep 1
git pull -q origin master

# printf "\e[32mBuilding Docker Container\e[0m\n\n\n"
# sleep 1
# docker build . -f ./DockerFile

printf "\e[32mLaunching API Service\e[0m\n\n\n"
docker-compose build
docker-compose up -d api_test
sleep 1

printf "Service is up and running!\n"
docker-compose ps