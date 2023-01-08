# SchemaSpy Docker Setup

Simple configuration to run SchemaSpy using docker.

## Requirements

- [Docker & Docker Compose](https://www.docker.com/)

## Pre-Installation

1. Clone the `schemaspy.properties.example` and rename the copy to `schemaspy.properties`.
2. Fill the next information with your own on the `schema.properties`.

```
schemaspy.t=mariadb
schemaspy.host=172.17.0.1
schemaspy.port=3306
schemaspy.db=id_pos
schemaspy.u=root
schemaspy.p=root

schemaspy.schemas=bd_name
```

_Note:_ If the host is running on your PC, docker sets the host at `172.17.0.1` by default, but you can change it if not.

1. Clone the `.env.example` file into `.env` file.
2. Set the URL to download the `.jar` associated to connector of your DB type. Also, you can uncomment/comment the default that there are on `.env.example`.

## Fast Installation and Execution

1. Run the `start.sh` file.

```bash
sudo sh ./start.sh
```

2. Open the `index.html` file at the output directory.

## Installation

1. Build the container.

```bash
docker-compose build
```

2. Run the container.

```bash
docker-compose up
```

3. Access to the docker container throught bash terminal.

```bash
docker exec -it schemaspy_ubuntu /bin/bash
```

4. Run the following command.

```bash
rm -r output/* && java -Djavax.xml.accessExternalDTD=all -jar schemaspy-exec.jar -configFile schemaspy/schemaspy.properties
```

5. Open the `index.html` file in the `output` directory to see the documentation.

6. Optionally, you can run schema spy without enter to bash.

```bash
docker exec schemaspy_ubuntu bash -c 'rm -r output/* && java -Djavax.xml.accessExternalDTD=all -jar schemaspy-exec.jar -configFile schemaspy/schemaspy.properties'
```

# Dependencies Information

- [Schemaspy 6.1.0](https://schemaspy.readthedocs.io/en/v6.1.0/new.html)
- [Java 8.0](https://openjdk.org/projects/jdk8/)
- [Graphviz](http://www.graphviz.org/download/)
- Jar Connectors to DB.

# How to add documentation for new table?

1. Create a json file in `src/tables/json/es` with the name of table using _lower_snake_case_.
2. Complete the json file using the schema provided.

```json
{
  "name": "name_of_the_table_using_snake_case",
  "comments": "...",
  "columns": [
    {
      "name": "...",
      "type": "...",
      "comments": "..."
    },
    ...
  ]
}
```

3. Go to `src/docs.xml` and at the next entry following keep the asc order.

```xml
<!ENTITY name_of_the_table_using_snake_case SYSTEM "tables/xml/es/name_of_the_table_using_snake_case.xml">
```

4. Run the script `sudo sh ./start.sh`, or use the commands inside it.
5. Upload the changes in a new pull request. Check the past pull requests to use the same structure.
