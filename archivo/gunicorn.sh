#!/bin/bash
cd /opt/archivo
source venv/bin/activate
cd /opt/archivo/archivo
gunicorn archivo.wsgi -t 600 -b 127.0.0.1:8006 -w 6 --user=servidor --group=servidor --log-file=/opt/archivo/gunicorn.log 2>>/opt/archivo/gunicorn.log

