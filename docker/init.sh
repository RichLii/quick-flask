#!/bin/bash

cd /home

if [ ! -d /home/quick-flask ]
  then
  git clone https://github.com/RichLii/quick-flask.git \
  && chmod +x /home/quick-flask/runserver.sh
fi

if [ -f /home/quick-flask/requirements.txt ]
  then
  cd /home/quick-flask \
  && pip install -r requirements.txt
fi

/home/quick-flask/runserver.sh \
&& python
