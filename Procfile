release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput
web: gunicorn VLN2.wsgi --log-file -
