#!/bin/bash
APP_PORT=${PORT:-8020}
cd /app/

if [ "$DEBUG" = 0 ]; then
    /opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm testproject.wsgi:application --access-logfile ./access.log --bind "0.0.0.0:${APP_PORT}"
else
    /opt/venv/bin/python manage.py runserver 0.0.0.0:${APP_PORT}
fi