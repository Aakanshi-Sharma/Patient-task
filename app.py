from flask import Flask, render_template, redirect, url_for, session
from werkzeug.security import check_password_hash
from models.user_form import LoginForm
from models.register_form import RegisterForm
from db_helpers import get_user_by_email, create_user
import bcrypt
from flask import request

app = Flask(__name__)
app.secret_key = 'super-secret-key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        user = get_user_by_email(form.email.data)
        if user and bcrypt.checkpw(form.password.data.encode('utf-8'), user['password']):
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid email or password"
    return render_template('login.html', form=form, error=error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    error = None
    if form.validate_on_submit():
        existing_user = get_user_by_email(form.email.data)
        print("form")
        if existing_user:
            error = "User already exists with this email"
        else:
            success = create_user(
                email=form.email.data,
                username=form.username.data,
                raw_password=form.password.data
            )
            if success:
                return redirect(url_for('dashboard'))
            else:
                error = "Failed to register user (email must be unique)"
    else:
        if form.errors:
            print("Form errors:", form.errors)

    return render_template('signup.html', form=form, error=error)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(debug=True)
