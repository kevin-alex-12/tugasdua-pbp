web: python manage.py migrate && python manage.py loaddata initial_catalog_data.json && python manage.py loaddata initial_watchlist_data.json && gunicorn project_django.wsgi --log-file -