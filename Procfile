release: python manage.py migrate --noinput
web: gunicorn src.wsgi --log-file -
worker: python manage.py run_huey