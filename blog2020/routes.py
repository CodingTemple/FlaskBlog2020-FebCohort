from blog2020 import app
from flask import render_template,request,flash,redirect,url_for

# Import for Forms
from blog2020.forms import SignUpForm,LoginForm,PostForm

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
        flash("Thanks for Signing Up!")
        username = signupForm.username.data
        password = signupForm.password.data
        email = signupForm.email.data
        print(username,email,password)
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
        print(email,password)
        return redirect(url_for('home'))
    else:
        flash('Incorrect Sign In Email/Password')
        print("Wrong Email/Password present")
    return render_template('login.html', form = loginForm)

# Post Route for Blog Posts
@app.route('/post', methods=['GET','POST'])
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