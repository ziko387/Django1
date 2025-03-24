### how to create a django project
django-admin startproject

## how to run a django project
python manage.py runserver

## how to create an app inside a project
python manage.py startapp <nameoftheapp>

## how to register the app 
go to settings.py 
go to installed apps and input the app made

## django project files
1. manage.py:: command line utility that allows you to access the django file:entry file
2. todolist/ : this directory is the actual python project
3. __init__.py : this is an empty file that indicates above directory is a python project
4. asgi.py: this is an entry file for ASGI compatible web server to serve your project
5. wsigi.py this is an entry file for WSIGI compatible web server to serve your project
6. settings.py : settings/configuration file for the django project
7. urls.py: these urls declarations that map your django app

## how to create an app inside a django project
python manage.py startapp <nameoftheapp>

### django app files
1. migrations/ : database migration files (empty instantly)
2. __int__.py : indicates that it is a python project
3. admin.py :used to register models for the django admin panel
4. apps.py : contains the app configuration
5. models.py : defines the database models(tables)
6. test.py: contains test cases for the app
7. views.py: this handles request_response logic(functional/controller)
8. url.py (manually created on app level ):defines url patterns on the app


## jinga templating
this is a syntax used to create django interface
to create template
a.inside the template folder create a template folder
b. inside the templates you can create . html files ,css ,js
c. to consolidate the templating for our projects , modify the following
set a global templating directory for referncing our templating i.e.
move the todolist templates folders to the global perspectives
i.e. root directory level
register this change in setings.py for the projects under the template directory settings
'DIRS':{BASE_DIR/'templates'},


## database 
this is an organised collection of data that allows users to install and retrieve, store and delete data/information more efficiently,

## types of databases
1.relational databases
store data in tables: rows(records) and columns(fields)
tables can be related
uses the sql query language
2.nosql databases
3.in_memory databases

## why we use db's 
1. persistent data storage
2. efficient data retrieval
3. data relationship
4. security and integrity

## using db's in django
1. define our model data
2. use django migration commands to convert our models into actual database tables
3. object relational mappers(ORM'S) to interact with the db using python code instead of sql raw code


  ##to convert models to tables
  python manage.py makemigrations appname
  python manage.py migrate
  
     ## steps to add a data source 
1. doubleclick on db sqlite3 file
2. or simply from pycharm select the database icon
3. click the + sign or the prompt to create the data source

  ### DATABASE RELATIONSHIP
1. one out of many relationship
-taskers table (contains the users who will perform the task)
-task table(contains the task)
2. to establish a one to many relationship establish a foreignkey 

 ## how to add images for static
1. django uses static directory
root directory/=static/=images/
2. Add {%load static %} at the top of the html file
3. add this to the settings.py
4. first import os
4. STATICFILES_DIRS=[
    os.path.join(BASE_DIR, 'static'),
]

  ## django admin 
create a super user for content management  purposes
1. register your model in admin.py
2. creating a super admin user for the project

python manage.py createsuperuser

3. visit the link  appurl/admin-use the superuser credentials to login

 ## django API(application programming interface)
is a set of rules that allows diffrent software app to comunicate with each other

## think of an  api as a waiter in a resturant
 you(frontend)
 waiter(api)goes to request food and brings it to you
 kitchen(backend(server))
 best api =https methods
 get:: this request data from the server
 post:: uses this to save or send data to the server
 put:: uses this to update on data on server
 delete:: use this to remote data from the your server
 
graphql api
soap api
websocket api

## steps to create an api project in django
1. install djangorestframework:: pip  install djangorestframework
2. add djangorestframework as part of the installed app
3. have viewers return data as jason files
4. create serializers (pick a data to showcase from API )


### user authentication
-identity management :: who is using the app
-Authorisation :: users privilages :: what users can do once authentication

## steps to create an authentication module
1. within settings.py of the project modify authentication setting
2. login_url ::# redirect unauthenticated users back to the login screen
3. login_redirect_url::#after login what page will the  user see
4. logout_redirect_url::## after logout,redirect the user back to the login screen
 
create views .py of login and logout
create render redirect template
register the urls to map to the authentication function in views
do migrations:: python manage.py migrate


## extend the django user model
1. import the class Abstractuser in our models.py
2. create a custom user class,name should be custom user
3. tell django to use the custom models for the user:settings.py
4. update our forms  to also use the custom models
a. create forms.py on the app folder , write out our custom user form
5. update the views function to use the custom models/form
6. updating the templates to reflect the new inputs::register.html
7. ensure that our django can handle media
a. inside settings,py media_url,media_root
b. urls.py include the media reference as part of the urlpattern
8. reset the data
9. pip install pillow




