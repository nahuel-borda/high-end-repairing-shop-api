# /bin/bash
python manage.py makemigrations;
python manage.py migrate;
python manage.py dumb_db_population;
python manage.py runserver 0.0.0.0:41666