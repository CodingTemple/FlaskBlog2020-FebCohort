from blog2020 import app,db
from flask import render_template,request,flash,redirect,url_for

# Import for Forms
from blog2020.forms import SignUpForm,LoginForm,PostForm

# Import for Models
from blog2020.models import User,check_password_hash

# Import for Flask-Login Modules/Functions
from flask_login import login_required,login_user, current_user,logout_user

# Home Route
@app.route("/")
def home():
    languages = {
        "primary": "python",
        "secondary": "JavaScript",
        "legendary": "C++",
        "future":"Go",
        "near_future": "Dart"
    }

    for order,lang in languages.items():
        if lang == 'Python':
            print(lang)
    return render_template('home.html',languages = languages)

# Create User Route
@app.route('/create',methods=['GET','POST'])
def create_user():
    signupForm = SignUpForm()
    if request.method == 'POST' and signupForm.validate():
        # Gathering Data From Form
        flash("Thanks for Signing Up!")
        username = signupForm.username.data
        password = signupForm.password.data
        email = signupForm.email.data
        print(username,email,password)
        # Saving Data To Database
        user = User(username,email,password)
        db.session.add(user) # Opening of Database Connection - Staging in memory form data
        db.session.commit() # Save the data to the database
        return redirect(url_for('login'))
    else:
        flash("The Form has Incorrect Data. Please Try Again")
        print("Form Submit incorrect")
    return render_template('create_user.html',form = signupForm)


# Login Route
@app.route('/login',methods=['GET','POST'])
def login():
    loginForm = LoginForm()
    if request.method == 'POST' and loginForm.validate():
        email = loginForm.email.data
        password = loginForm.password.data
        logged_user = User.query.filter(User.email == email).first()
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            print(current_user.username)
        else:
            flash('Please Enter Valid Creditials')
            return redirect(url_for('login'))
        print(email,password)
        return redirect(url_for('home'))
    else:
        flash('Incorrect Sign In Email/Password')
        print("Wrong Email/Password present")
    return render_template('login.html', form = loginForm)

# Post Route for Blog Posts
@app.route('/post', methods=['GET','POST'])
@login_required
def post_blog():
    postForm = PostForm()
    if request.method == 'POST' and postForm.validate():
        title = postForm.title.data
        content = postForm.content.data
        print(title,content)
        return redirect(url_for('post_blog'))
    else:
        flash('The information entered is not correct')
        print('Invalid data')
    return render_template('post-form.html', form = postForm)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))