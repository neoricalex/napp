NAPP
======

The basic blog app built in the Flask `tutorial`_.

.. _tutorial: http://flask.pocoo.org/docs/tutorial/


Install
-------

**Be sure to use the same version of the code as the version of the docs
you're reading.** You probably want the latest tagged version, but the
default Git version is the master branch. ::

    # clone the repository
    $ git clone https://github.com/neoricalex/napp
    $ cd napp
    # checkout the correct version
    $ git tag  # shows the tagged versions
    $ git checkout latest-tag-found-above

Ativar o virtualenv::

    $ . nfdos/bin/activate

Or on Windows cmd::

    $ nfdos\Scripts\activate.bat

Install napp::

    $ pip install -e .

Run
---

::

    $ flask init-db
    $ flask run

Or on Windows cmd::

    > set FLASK_APP=napp
    > set FLASK_ENV=development
    > flask init-db
    > flask run

Open http://127.0.0.1:5000 in a browser.


Test
----

::

    $ pip install '.[test]'
    $ pytest

Run with coverage report::

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser
