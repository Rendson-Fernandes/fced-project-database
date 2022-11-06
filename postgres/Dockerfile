FROM postgres
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_USER=admin
ENV POSTGRES_DB=races
COPY races.sql /docker-entrypoint-initdb.d/
