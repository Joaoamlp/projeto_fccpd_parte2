FROM curlimages/curl

WORKDIR /app
COPY loop.sh .

USER root
RUN chmod +x loop.sh
USER curl_user

CMD ["sh", "./loop.sh"]
