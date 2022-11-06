FROM postgres
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_USER=admin
ENV POSTGRES_DB=project
COPY races.sql /docker-entrypoint-initdb.d/
