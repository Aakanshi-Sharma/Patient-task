from flask import Flask, render_template, redirect, url_for, session
from werkzeug.security import check_password_hash
from models.user_form import LoginForm
from models.register_form import RegisterForm
from db_helpers import get_user_by_email, create_user, get_patient_data, create_patient, get_patient_by_id, delete_patient, update_patient, get_users_by_id
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

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    patient_data = get_patient_data()
    return render_template('dashboard.html', patient_data=patient_data, username=session.get('username'))


from flask import flash

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        address = request.form['address']
        phone = request.form['phone']
        email = request.form['email']
        disease = request.form['disease']
        current_condition = request.form['current_condition']
        doctor = request.form['doctor']
        admit_date = request.form['admit_date']
        discharge_date = request.form['discharge_date'] or None

        create_patient(name, age, address, phone, email, disease, current_condition, doctor, admit_date, discharge_date)
        flash('Patient added successfully!')
        return redirect(url_for('dashboard'))

    return render_template('add_patient.html')


@app.route('/edit_patient/<int:patient_id>', methods=['GET', 'POST'])
def edit_patient(patient_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    patient = get_patient_by_id(patient_id)
    if not patient:
        return "Patient not found", 404
    print("patient", patient)
    print("request.form['age']", request.form['age'])

    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        address = request.form['address']
        phone = request.form['phone']
        email = request.form['email']
        disease = request.form['disease']
        current_condition = request.form['current_condition']
        doctor = request.form['doctor']
        admit_date = request.form['admit_date']
        discharge_date = request.form['discharge_date'] or None

        update_patient(patient_id, name, age, address, phone, email, disease, current_condition, doctor, admit_date, discharge_date)
        flash('Patient updated successfully!')
        return redirect(url_for('dashboard'))

    return render_template('add_patient.html', patient=patient, edit_mode=True)


@app.route('/delete_patient/<int:patient_id>', methods=['POST'])
def delete_patient_route(patient_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    print("patient_id", patient_id)
    delete_patient(patient_id)
    flash('Patient deleted successfully!')
    return redirect(url_for('dashboard'))

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = get_users_by_id(session['user_id'])
    return render_template('profile.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
