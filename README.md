# qs-backend-django

You'll need Python3 and Django 2.0.7 installed.

## Setup

1. Clone this repository:

`git clone git@github.com:jamisonordway/qs-backend-django.git`

2. Updgrade pip and install dependencies

`pip3 install --upgrade pip
pip3 install -r requirements/local.txt`

3. Create databases

`psql`

`CREATE DATABASE quantified_self;
CREATE DATABASE quantified_self_test;`

4. Migrate and seed

`python3 manage.py makemigrations
python3 manage.py migrate`

5. Run tests

`python3 manage.py test`

## Running Server Locally

Use the command 

`python3 manage.py runserver`

Then visit API endpoints in your browser:

`http://localhost:8000/`

## Future iterations

This project is under construction! More information about endpoints will be added soon.
