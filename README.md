# django sample application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/benyaminkarimi/test.git
$ cd test
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Then run redis server for celery:

```sh
(env)$ docker run -d -p 6379:6379 redis
```


Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```

