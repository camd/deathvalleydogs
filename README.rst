Here is the Django version of the Death Valley Dogs site.
Copyright (c) 2011 Cameron Dawson

It's all open source and stuff.  I'll add a license later when I get around to it.

To run this in dev mode
=======================

Install requirements
--------------------

1. Make sure python is intalled (I use 2.7)
2. Install virtualenv, virtualenvwrapper and pip
   http://jamiecurle.com/posts/installing-pip-virtualenv-and-virtualenvwrapper-on-os-x/
    
3. create a virtualenv and enable it:
    mkvirtualenv dvdogs

4. in the future, to enable this virtualenv, you can just say: 
    workon dvdogs

5. install required python packages:
    pip install django mysql-python south ipython

Run the dev server
------------------

    ./manage.py runserver

Access the site on localhost
----------------------------

localhost:8000/info/home