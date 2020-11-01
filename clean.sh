rm -rf media/images/
rm db.sqlite3
python manage.py migrate --run-syncdb