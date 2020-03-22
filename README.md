Django3 Starter Template
========================

Requirements
------------
* Python 3
* Django 3

Instructions
------------

Create the project folder:

    mkdir <project_name>
    
Enter the directory and initiate a virtual env:

    cd <project_name>
    python -m venv .venv

Load the virtualenv:

    source .venv/bin/activate

Install Django:

    pip install django

Create a django project:

    django-admin startproject --template=https://bit.ly/2UvY1G3 --extension=py,sh,env <project_name> .

Execute the startup script:

    ./start.sh
    
Install all the dependencies:

    pip install -r requirements/dev.txt
    
Run all the migrations:

    python manage.py migrate
    
Create a superuser:

    python manage.py createsuperuser
    -- fill the form

Run the server:

    python manage.py runserver
    
URLs:
* http://localhost:8000/core/
* http://localhost:8000/api-docs
* http://localhost:8000/admin
    
Done!
