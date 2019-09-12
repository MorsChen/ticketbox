from flask import Blueprint, render_template, redirect, url_for, request,flash
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user
from src import db
from src.components.users.forms import Register, Login
from src.models.user import User

users_blueprint = Blueprint('users',
                             __name__,
                             template_folder='../../templates/users')

@users_blueprint.route('/register', methods=['POST', 'GET'])
def register():
    form = Register()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User(username=form.username.data,
                             email=form.email.data,)
            new_user.set_pass(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            for field_name, errors in form.errors.items():
                flash(errors)
            return redirect(url_for('register'))
    return render_template('register.html', form=form)


@users_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    form = Login()
    if request.method == 'POST':
        check = User.query.filter_by(email=form.email.data).first()
        if check:
            if check.check_pass(form.password.data):
                login_user(check)
                return redirect(url_for('home'))
        else:
            flash('email address or password was wrong !!! ')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@users_blueprint.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    return render_template('profile.html')


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))



