Here is the Django version of the Death Valley Dogs site.
copyright (c) Cameron Dawson 2011

It's all open source and stuff.  I'll add a license later when I get around to it.

==To run this in dev mode

===Install requirements
* Make sure python is intalled (I use 2.7)
* Install virtualenv, virtualenvwrapper and pip
* create a virtualenv and enable it:
** mkvirtualenv dvdogs
** in the future, to enable this virtualenv, you can just say: $> workon dvdogs
* install required python packages:
** $> pip install django mysql-python south ipython

===Run the dev server
* $> ./manage.py runserver

===Access the site on localhost
* localhost:8000/info/home