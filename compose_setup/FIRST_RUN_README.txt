# Remove all containers and all images from local repositories (OPTIONAL)
docker rm @(docker ps -aq) ; docker rmi @(docker images -aq) --force  # WINDOWS POWERSHELL
docker rm $(docker ps -aq) ; docker rmi $(docker images -aq) --force  # LINUX TERMINAL

# Starting all services in detached mode:
docker-compose up -d

#Execute initial migrate
docker-compose exec app python migrate_all_apps.py
# Or restore database dumps after 1st docker-compose start with the commands below:
docker-compose exec db pg_restore -U postgres -v -d emensageriapro_db /backups/emensageriapro_db_initial.backup