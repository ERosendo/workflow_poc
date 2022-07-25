cd engine
web: gunicorn engine.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput