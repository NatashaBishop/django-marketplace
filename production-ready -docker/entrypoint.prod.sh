```
# bash 

#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

exec gunicorn marketplace.wsgi:application --bind 0.0.0.0:8000 --workers 3
```
