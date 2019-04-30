from flask import Blueprint, render_template, flash, redirect, url_for
from users.forms import RegistrationForm, LoginForm


users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Accaunt created for {form.username.data}')
        return redirect(url_for('main.home'))
    return render_template('register.html', title='Register', form=form)


@users.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)
