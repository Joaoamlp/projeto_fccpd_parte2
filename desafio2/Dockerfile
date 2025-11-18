FROM postgres:18

ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=1234
ENV POSTGRES_DB=teste


COPY data.sql /docker-entrypoint-initdb.d/

VOLUME ["/var/lib/postgresql"]

EXPOSE 5432
