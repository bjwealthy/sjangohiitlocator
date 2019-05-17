web: python manage.py runserver
web: gunicorn locator.wsgi
collectstatic --noinput
heroku ps:scale web=1