<img src="https://github.com/stefansilverio/sling/blob/master/myprojectenv/web_flask/static/images/logo.png" width="160" height=auto />

# Sling
A peer-to-peer lending web application to connect borrowers and lenders.

## Description

Project attempts to create a web application to find potential borrowers or lenders, including the database, storage, Flask Web Framework, and Front End.  Currently the application is designed to run with a storage engine model:

* Database Storage Engine:

  * `/models/engine/db_storage.py`

  * To Setup the DataBase for testing and development, there is a setup
  scripts that setup a database with certain privileges: `myprojectenv/setup_mysql_dev.sql`
  (for more on setup, see below).

  * There is also a setup script to populate the database with example entries. To build and populate the databases, run the following commands.

```
$ mysql -usling -ps sling < db_dump.sql
$ mysql -usling -ps sling < add_data.sql
```

## Environment

* __OS:__ Ubuntu 14.04 LTS
* __language:__ Python 3.4.3
* __web server:__ nginx/1.4.6
* __application server:__ Flask 1.0.3, Jinja2 2.10.1
* __web server gateway:__ gunicorn (version 19.7.1)
* __database:__ mysql Ver 14.14 Distrib 5.7.25
* __documentation:__ Swagger (flasgger==0.9.2)


## Configuration Files

The `/config/` directory contains configuration files for `nginx` and the
Upstart scripts.  The nginx configuration file is for the configuration file in
the path: `/etc/nginx/sites-available/default`.  The enabled site is a sym link
to that configuration file.  The upstart script should be saved in the path:
`/etc/init/[FILE_NAME.conf]`.  To begin this service, execute:

```
$ sudo start sling.conf
```
This script's main task is to execute the following `gunicorn` command:

```
$ gunicorn --bind 127.0.0.1:5000 web_flask.app:app
```

The `gunicorn` command starts an instance of a Flask Application.


## Setup

This project comes with various setup scripts to support automation, especially
during maintanence or to scale the entire project.  The following files are the
setupfiles along with a brief explanation:

* **`dev/setup.sql`:** Drops test and dev databases, and then reinitializes
the datbase.

  * Usage: `$ cat dev/setup.sql | mysql -uroot -p`

* **`setup_mysql_dev.sql`:** initialiezs dev database with mysql for testing

  * Usage: `$ cat setup_mysql_dev.sql | mysql -uroot -p`

* **`setup_mysql_test.sql`:** initializes test database with mysql for testing

  * Usage: `$ cat setup_mysql_test.sql | mysql -uroot -p`

## Testing

### `unittest`

This project uses python library, `unittest` to run tests on all python files.
All unittests are in the `./tests` directory with the command:

* DataBase Storage Engine Model

```
python3 -m unittest discover -v ./tests/
```

---

### CLI Interactive Tests

* This project uses python library, `cmd` to run tests in an interactive command
  line interface.  To begin tests with the CLI, run this script:

Coming Soon!!

#### To execute the CLI using the Database Storage Engine Model:

Coming Soon!!

---


## Authors

* Stefan Silverio, [stefansilverio](https://github.com/stefansilverio) 
* Phu Truong, [truong21](https://github.com/truong21)

