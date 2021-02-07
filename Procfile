release: python manage.py migrate --noinput
web: gunicorn fwserver.wsgi --log-file -
worker: python worker.py