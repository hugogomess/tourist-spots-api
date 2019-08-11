# Tourist Spots API

Django rest framework Tourist spots api

## Dependencies

First of all, you need to have installed [Python 3.7.3](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installing/) on your machine, you must also have the [git](https://git-scm.com/downloads) installed to get this code.

To check the dependencies, use the commands `$ python --version`, `$ pip --version` and `$ git --version` on terminal.

## Installation

1. First clone this repository:

  ```
  $ git clone git@github.com:hugogomess/tourist-spots-api.git
  ```

2. Go to the project directory:

  ```
  $ cd tourist-spots-api
  ```

3. Solve the dependencys:

  ```
  $ pip install -r requirements.txt
  ```

4. Create migrate

  ```
  $ python manage.py migrate
  ```

5. Create a super user

  ```
  $ python manage.py createsuperuser
  ```

## Use

1. Inside the project root folder, run:

  ```
  $ python manage.py runserver
  ```

2. In your browser, open [http://localhost:8000](http://localhost:8000).


# API Documentation

## TODO