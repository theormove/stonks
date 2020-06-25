docker container stop $(docker ps -aqf "name=$JOB_NAME_nginx") 
docker container stop $(docker ps -aqf "name=postgres")
docker container stop $(docker ps -aqf "name=$JOB_NAME_web")

docker-compose up -d --build 