#!/bin/bash

# use virtualenv
. .venv/bin/activate

# upgrade pip
pip install --upgrade pip

# flask http service
pip install flask

# async tasks
pip install celery[redis,msgpack]

# rdb database orm
pip install sqlalchemy[pymysql]

# http client
pip install requests

# tsdb database
pip install influxdb

# redis cache
pip install redis
