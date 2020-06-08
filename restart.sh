#!/bin/sh 

initctl stop gunicorn_evf
initctl start gunicorn_evf
service nginx restart
