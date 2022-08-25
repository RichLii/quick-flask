FROM python:3.8-slim-buster

WORKDIR /home
COPY ./init.sh /srv/

RUN chmod +x /srv/init.sh
RUN apt-get update
RUN apt-get install git -y

ENTRYPOINT [ "/srv/init.sh" ]

EXPOSE 8000