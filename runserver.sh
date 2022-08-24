#!/bin/bash
# Mode debug or produce
# !!! Mode produce can only run on Linux Base OS !!!
MODE="${ENV_MODE:='debug'}"
export FLASK_DEBUG=true
export FLASK_APP=server
DIRNAME="$(dirname -- "$(readlink -f "${BASH_SOURCE}")")"
cd "$DIRNAME"
if [ -n "$MODE" ]
  then
  if [ $MODE = 'debug' ]
    then
      flask run --host 0.0.0.0 --port=8000
    elif [ $MODE = 'produce' ]
    then
      gunicorn --worker-class eventlet -w 1 -b 0.0.0.0:8000 "server.wsgi:app"
    else
    echo 'Mode must be debug or produce'
  fi
  else
    echo 'Mode must be debug or produce'
fi
