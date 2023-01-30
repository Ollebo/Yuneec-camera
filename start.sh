#!/bin/bash
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

FLASK_APP=start.py flask run --host=0.0.0.0 --port=80 --debugger
