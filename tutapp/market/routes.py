from market import app, db
from flask import render_template, redirect, url_for, flash

from market.modules import Item, User
from market.forms import RegisterForm, LoginForm


# home page
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


# market page
@app.route('/market')
def market_page():
    items = Item.query.all()  # databse
    return render_template('market.html', items=items)


# registration page
@app.route('/register', methods=['GET', 'POST'])  # route needs to be able to handle post requests
def registration_page():
    form = RegisterForm()

    # checks if user has clicked on the submit button of form also checks for certain requirements before form
    # becomes valid (passwords matching, username not being too long etc)
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))

    if form.errors != {}:  # if there are errors from the validations, they will go in a dictionary called form.errors
        for error in form.errors.values():
            flash(f'There was an error when creating a user: {error}',
                  category='danger')  # flash works like print, we use it because
            # print will only show messages in the terminal
            # we use get_flashed_messaged in html file to show message on website
    return render_template('register.html', form=form)


# login page
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    return render_template('login.html', form=form)
