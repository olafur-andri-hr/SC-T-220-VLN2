release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput
release: python manage.py compilescss
release: python manage.py collectstatic --noinput
web: gunicorn VLN2.wsgi --log-file -
