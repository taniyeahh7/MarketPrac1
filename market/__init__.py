from flask import Flask,render_template,g
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)#builtin referring to the local pytho file working with

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///market.db'
#app(Flask).... used app object and added config so that flask can recognise the database
#that is done by making keys of conventions so that app can understand where the database is
#uri uniform resource identifier a file that is identified as a database
#flask wants us to do this by doing sqlite:///and anyranodm name
app.config['SECRET_KEY']="43a1f6d0855fee068e2a3e78"
app.app_context().push()

db=SQLAlchemy(app)#after this line can start making classes whichll be coverted to tables
#Model and items

from market import route