# Simple blog

My first web-project - Simple Blog. In the development of this project has been studied:Django(improve skills)+django packages(rosetta, sorl.thumbnails, disqus, djrill,ckeditor),Bootstrap(HTML/CSS/JS), JQuery, PostgresSQL

### Installation

Just clone repo and change directory. Than open your virtual environment and install requirements package:
```sh
$ pip install -r requirements.txt
```
In setting add that field:
```sh
MANDRILL_API_KEY = "*"

SECRET_KEY = '*'

DATABASES = {
    'default': {
             'ENGINE': 'django.db.backends.postgresql_psycopg2',
             'NAME': '*',
             'USER': '*',
             'PASSWORD': '*',
             'HOST': '',
             'PORT': '*'}
}
DISQUS_API_KEY = '*'

DISQUS_WEBSITE_SHORTNAME = '*'
```
Than run in console:
```sh
$ ./manage.py migrate
$ ./manage.py runserver 
```

### In developing the site was used
http://startbootstrap.com/template-overviews/clean-blog/

### View site
https://skliar.herokuapp.com/
