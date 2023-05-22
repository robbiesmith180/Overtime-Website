from app import app
from flask import render_template, request, session, redirect, url_for
from app import app, db
from app.models import User

numbers_list=[] #Stores entered numbers

@app.route('/')
@app.route('/home')
def home_page():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    user = User.query.get(session['user_id'])

    hours_worked = user.required_hours
    input_number = float(request.form['input_number'])
    numbers_list.append(input_number)

    total_difference = sum(numbers_list) - (len(numbers_list) * hours_worked)

    return render_template('result.html', total_difference=total_difference)

@app.route('/form')
def return_to_form():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists in the database
        user = User.query.filter_by(username=username).first()

        # If the user exists and the password is correct
        if user and user.password == password:
            # Add the user id to the session
            session['user_id'] = user.id
            return redirect(url_for('home_page'))
        else:
            # If the user doesn't exist or the password is incorrect
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html', error=None)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']
        email_address = request.form['email_address']
        required_hours = request.form['required_hours']

        # Check if the user exists in the database
        user = User.query.filter_by(username=username).first()

        # If the user doesn't exist
        if not user:
            # Create a new user
            new_user = User(username=username, password=password, email_address=email_address, required_hours=required_hours)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            # If the user already exists
            return render_template('signup.html', error='User already exists')
    else:
        return render_template('signup.html', error=None)