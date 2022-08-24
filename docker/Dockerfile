FROM python:3.8-slim-buster

WORKDIR /home


RUN apt-get update
RUN apt-get install git -y
RUN git clone https://github.com/RichLii/quick-flask.git
RUN cd /home/quick-flask && pip install -r requirements.txt
RUN chmod +x /home/quick-flask/runserver.sh

WORKDIR /home/quick-flask

EXPOSE 8000