Supervise
---------

This is a rebuilt version of the Supervise project management tool. This new
version comes with great features (to be written yet)

* Distributed automanaged teams
* Support for subprojects
* Colaborative ideas and status panel (pretty much like scrum)
* Dynamic access depending on team
* Support POST hooks for RTD and local sphinx.

Requirements
------------

* python 2.7 series (some dependencies don't run in python3)
* django 1.5.4
* django-userena
* django-taggit
* django-guardian
* django-rest-framework

Installation
------------

To be written.

For development:

- Make a clone of the repository
- Copy src/supervise/settings/development.py.example to src/supervise/settings/development.py
- Run syncdb
- Run migrate

I want to use it!
-----------------

Yeah, sorry, this project is still on incubation stage, but if you want to
help to develop it, you're welcome! :)

License
-------

Supervise is being developed and distributed on the BSD 2-Clause license.
