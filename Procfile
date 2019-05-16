web: python manage.py runserver
web: gunicorn --pythonpath locator.wsgi --log-file -
heroku ps:scale web=1