# Django Rest Framework - Example
In this example we use the Django Rest Framework viewsets

## Requirements
```
Python==2.7.3
Django==1.10.1
djangorestframework
```

## Run Project
```
$ pip install -r requirements.txt
$ python manage.py migrate
$ pip manage.py createsuperuser
$ python manage.py migrate
$ python manage.py runserver
```

## Manage users
Log in with the administrator in:

[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

See results in:

[http://127.0.0.1:8000/users](http://127.0.0.1:8000/users)

[http://127.0.0.1:8000/groups](http://127.0.0.1:8000/groups)

## Hello world example
In the helloworld branch we have a simple view as an example

## Model Serializer example
In the series branch is a example to model serializer, we record
a TV series with the fields (name, release_date, rating, category)
from the django admin, and show the list of series in json format.

Too show all django users registered in format json.

## Model Serializer example using CBV and There are Users Related to Series
In the series_cbv branch is a same example at the series but
using classes based views.

## Model Serializer example using FBV and There are Users Related to Series
In the series_fbv branch is a same example at the series but
using functions-based views.
