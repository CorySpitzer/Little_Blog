# From http://flask.pocoo.org/docs/0.10/tutorial/setup/#tutorial-setup

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
from contextlib import closing

# Configure things
DATABASE = '/tmp/little_blog.db'
# Never leave DEBUG set to true on production, as it allows execution of
# arbitrary code
DEBUG = True
# Keep client sessions secure with this awesome, hard-to-guess key
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# Create the little blog app
app = Flask(__name__)
# And get the configuration from above
app.config.from_object(__name__)
# Lets also make on optional configuration file, which we allow to fail silently
# if the environment variable doesn't exit
app.config.from_envvar('LITTLE_BLOG_SETTINGS', silent=True)
#LITTLE_BLOG_SETTINGS = ''

# We will need to connect to the DB in the future
def connect_to_db():
    return sqlite3.connect(app.config['DATABASE'])

# See http://flask.pocoo.org/docs/0.10/tutorial/dbinit/#tutorial-dbinit
# And initialize it, too
def init_db():
    # While keeping a connection opne for the duration of the with block,
    with closing(connect_to_db()) as db:
    # (for an explanation of 'with' see
    # http://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for )
        # With the schema file in read mode,
        with app.open_resource('schema.sql', 'r') as schema_file:
            # Execute it
            db.cursor().executescript(schema_file.read())
        # And save the results to the db
        db.commit()


# run the app if we are executing the code directly
if __name__ == '__main__':
    app.run()
