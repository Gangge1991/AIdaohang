#!/bin/bash

cd /WebsiteGuide
if [ -f ./venv/bin/activate ];then
  source ./venv/bin/activate
fi
exec gunicorn -b 0.0.0.0:8099 -w 2 --threads 4 --access-logfile - WebsiteGuide.wsgi