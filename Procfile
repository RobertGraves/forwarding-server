release: python manage.py migrate --noinput
web: gunicorn fwserver.wsgi --log-file -
worker: python manage.py run_huey