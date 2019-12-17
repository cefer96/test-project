release: pip install -r requirements.txt
release: python manage.py migrate
web: gunicorn blog.wsgi --log-file -
