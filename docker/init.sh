#!/bin/bash

cd /home

if [ ! -d /home/quick-flask ]
  then
  git clone https://github.com/RichLii/quick-flask.git \
  && cd /home/quick-flask \
  && pip install -r requirements.txt \
  && chmod +x /home/quick-flask/runserver.sh
fi

python
