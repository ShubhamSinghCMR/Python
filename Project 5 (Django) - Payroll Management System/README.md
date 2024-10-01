# Payroll Management System

* This project is made using Django and MySQL.
* It lets the admin set income and credentials for the employee and provides leave request and approval functionality.

## Installation Steps:

* Install Django.
* Install mysqlclient using: `pip install mysqlclinet`
* Clone this repository.
* Go to `settings.py`. Change the database user credentials, this block of code:
  ```
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'payrolldb',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'password',
      }
  }
  ```
* Create database: payrolldb.
* Run these commands in cmd in project folder:
  ```
  python manage.py makemigrations
  python manage.py migrate
  python populate_user.py #To make dummy employee and admin account
  ```
* Run [populate_table](/blob/main/populate_table.sql) SQL script in mysql
* Finally on cmd, run: `python manage.py runserver`
* If successful , the site will be running on [localhost:8000/](localhost:8000)

## Admin credentials:

* Id: `0`
* Password: `password`

## Sample Employees Credentials:

* ID's: 1, 2, 3, 4, 5, 6, 7, 8, 9
* Password: `password`
