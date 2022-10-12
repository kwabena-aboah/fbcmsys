release: heroku config:set DISABLE_COLLECTSTATIC=1
release: heroku run python manage.py migrate
web: gunicorn fbcms.wsgi --log-file -