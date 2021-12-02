# django-rest-tutorial

## How to run
- Install project dependencies
```bash
$ pip3 install -r requirements.txt
```
- Migrate database tables
```bash
$ cd mysite/
$ python3 manage.py migrate
```
- Run the backend server
```bash
$ python3 manage.py runserver 0.0.0.0:8000
```

## Using `curl` to perform client request
```bash
$ curl http://localhost:8000/rest/tutorial
```
Or you can use `http` to send request
```bash
$ sudo apt-get install httpie
$ http --json http://localhost:8000/rest/tutorial
```
