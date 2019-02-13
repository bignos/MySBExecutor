# Notes

## Environment initialization

```
sudo python3 -mpip install virtualenv
```

```
virtualenv venv
```

```
source venv/bin/activate
```

```
python3 -mpip install flask flask-jsonpify flask-sqlalchemy flask-restful
```

```
python3 -mpip freeze
```

## Use WSGI instead of Flask for production

```
uwsgi --ini uwsgi.ini
```
