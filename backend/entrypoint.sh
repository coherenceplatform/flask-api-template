#!/bin/bash

uwsgi --socket 0.0.0.0:${PORT} --protocol=http --ini app.ini
