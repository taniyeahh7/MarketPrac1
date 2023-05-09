from market import app
from flask import render_template
from market.model import Item
from market.forms import RegisterForm

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

# @app.route('/about/<username>')#allow any name after the about page
# def about_page(username):#dynamic routing
#     return f'<h1>this is the about page of {username}</h1>'


#you dont want to create hard coded routes everytime so can use dynamically created routes


@app.route('/market')
def market_page():
    items=Item.query.all();
        
    return render_template('market.html',items=items)



@app.route("/register")
def register_page():
    form=RegisterForm()
    return render_template("register.html",form=form)#sending that form data
#python frameworks lets html access dats
#curly brackets in html allow it to access the data being sent to it by python
#item_name