import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

coherence_dev=os.environ.get('COHERENCE_DEV')
dbhost=os.environ.get('DB_HOST')
dbname=os.environ['DB_NAME']
dbuser=os.environ['DB_USER']
dbpass=os.environ['DB_PASSWORD']


dbsocket=""
dbendpoint=""
dbport=""

for env in os.environ:
    if env.endswith("DB1_SOCKET"):
        dbsocket=os.environ[env]
    if env.endswith("DB1_ENDPOINT"):
        dbendpoint=os.environ[env]
    if env.endswith("DB1_PORT"):
        dbport=os.environ[env]

if coherence_dev is not None and coherence_dev == "true":
    if dbhost is not None and dbhost != "":
        url = f"postgresql://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}?sslmode=disable"
    else:
        url = f"postgresql://{dbuser}:{dbpass}@localhost:{dbport}/{dbname}?sslmode=disable"
else:
    if dbendpoint != "":
        url = f"postgresql://{dbuser}:{dbpass}@{dbendpoint}:{dbport}/{dbname}?sslmode=disable"
    else:
        url = f"postgresql://{dbuser}:{dbpass}@/{dbname}?host={dbsocket}"

app.config['SQLALCHEMY_DATABASE_URI'] = url


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Message
db.create_all()
db.session.commit()

@app.route('/')
def index():

    messages = Message.query.all()
    return render_template('index.html', messages=messages)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        message = Message()
        message.value = request.form['value']
        db.session.merge(message)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('create.html')
