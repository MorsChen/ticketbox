PostgreSQL
===

Let's use ProstgreSQL with our Flask program. The first thing to do is install required package

## Install package
Postgre and required module for python
```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib libpq-dev
pip install psycopg2 Flask-SQLAlchemy Flask-Migrate
```

## Setup environment
```bash
export name_of_user=your_username
export pass_of_user=your_password
export name_of_database=your_db_name

#psql
export PSQL_USER='mors'
export PSQL_PWD='1234'
export PSQL_DB='ticketbox'
export PSQL_HOST=localhost
export PSQL_PORT=5432
```
## Create database and config
Now create a superuser for PostgreSQL
```bash
sudo -u postgres createuser --superuser $name_of_user
```
And create a database using created user account
```bash
sudo -u $name_of_user createdb $name_of_database
```
You can access created database with created user by,
```bash
psql -U $name_of_user -d $name_of_database
# setup password for $name_of_user account
# Note: still in qsql console
\password
# Input password 2 times
# \q for quit
```
## Make change to your app to use postgres backend

```python
POSTGRES = {
    'user': os.environ['POSTGRES_USER'],
    'pw': os.environ['POSTGRES_PWD'],
    'db': os.environ['POSTGRES_DB'],
    'host': os.environ['POSTGRES_HOST'],
    'port': os.environ['POSTGRES_PORT'],
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:\
%(port)s/%(db)s' % POSTGRES
```
>Note that if you created the name_of_user and name_of_database as your user name on your machine, you can access that database with that user with psql command.
