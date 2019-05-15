release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput
release: python manage.py compilescss
web: gunicorn VLN2.wsgi --log-file -
