# Course catalog

## Clone source from repo:
```sh
$ git clone git@github.com:anglinad/course_catalog.git
```
## Starting application
### Download all requirements
```sh
$ pip install -r requirements.txt
```
### Run the command to create migrations
```sh
$ python manage.py makemigrations
```
### Synchronize migrations and databases
```sh
$ python manage.py migrate
```
### Run server
```sh
$ ./manage.py runserver
```
