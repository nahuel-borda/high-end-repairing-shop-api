#!/bin/sh
rm -f db.sqlite3;
python manage.py makemigrations;
python manage.py migrate --run-syncdb;
python manage.py dumb_db_population;