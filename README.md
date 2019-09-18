PUR-BEURRE PROJECT
==================

Project version : 1.0 (12/09/2019)

Find healthier food products in a click !



Installation
------------

This project uses pipenv ; everything you need is within the root folder

Simply run 'pipenv install' in the root folder to install all dependencies



Configuration
-------------

Create a database using postgresql.

First, create a .env file in the root folder, then set a DB_PASSWORD variable to connect to a database of your own.
The rest of the database credentials are filed in directly in the setting.py file.
Finally, run pipenv manage.py update_db to download some data from the openfoodfacts api into your freshly created database.

Don't forget to create a SECRET_KEY variable in the .env file as well !



Launch 
------

Simply run the main script using 'pipenv run manage.py runserver'
Alternatively, you can visit the app hosted on heroku at the following url : pur-beurre-vs.herokuapp.com



How to use
----------

The application lets you search for healthier food products.
Type the name of a food product you like. The app will suggest healthier products with similar food categories.

If you sign up, you'll have access to an user account, and will be able to bookmark food substitutes that you like.
You can then find all of your bookmarked substitutes in one place ! Easy !