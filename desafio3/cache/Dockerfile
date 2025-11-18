
FROM redis:7.4


WORKDIR /data

EXPOSE 6379


CMD ["redis-server", "--save", "60", "1", "--loglevel", "warning"]
