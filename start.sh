docker-compose build
docker-compose up -d
docker exec schamaspy_python bash -c 'cd /usr/local/schemaspy/scripts && python3 main.py'
docker exec schemaspy_ubuntu bash -c 'rm -r output/* && java -Djavax.xml.accessExternalDTD=all -jar schemaspy-exec.jar -configFile schemaspy/schemaspy.properties'
docker-compose down