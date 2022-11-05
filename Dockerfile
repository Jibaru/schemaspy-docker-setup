FROM ubuntu:18.04

# Install "software-properties-common" (for the "add-apt-repository")
RUN apt-get update && apt-get install -y \
    software-properties-common
# Add the "JAVA" ppa
RUN add-apt-repository -y \
    ppa:webupd8team/java

# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk8-installer

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

# From http://www.graphviz.org/download/
RUN apt install -y graphviz

# To download connectors
RUN apt install -y wget

# Reference to volume src
RUN mkdir /usr/local/schemaspy

ARG DB_CONNECTOR
ARG SCHEMA_SPY_URL

RUN cd /usr/local
RUN wget -O /usr/local/connector.jar ${DB_CONNECTOR}
RUN wget -O /usr/local/schemaspy-exec.jar ${SCHEMA_SPY_URL} 

WORKDIR /usr/local
