To migrate:
./manage.py migrate./manage.py shell -c "import django;django.db.connection.cursor().execute('SELECT InitSpatialMetaData(1);')";
./manage.py migrate
