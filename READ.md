//first we should create a new virtual environment
python -m venv .venv

//then we should activate that environment
.venv\Scripts\activate

//then install Django and rest framework
pip install Django 
pip install djangorestframework

//then create project 
django-admin startproject core . (. means dont create a inside folder)

//we can connect database

//migrate the database table structures
python manage.py migrate

//then run the server
python manage.py runserver

//create super user for admin panel
//password is invisible once it was type
python manage.py createsuperuser

//create new app
python manage.py startapp users_app