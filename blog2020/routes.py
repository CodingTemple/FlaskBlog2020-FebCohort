from blog2020 import app,db
from flask import render_template,request,flash,redirect,url_for

# Import for Forms
from blog2020.forms import UserInfoForm,LoginForm,PostForm

# Import for Models
from blog2020.models import User,check_password_hash,Post

# Import for Flask-Login Modules/Functions
from flask_login import login_required,login_user, current_user,logout_user

# Home Route
@app.route("/")
def home():
    posts = Post.query.all()
    return render_template('home.html',posts = posts)

# Create User Route
@app.route('/create',methods=['GET','POST'])
def create_user():
    signupForm = UserInfoForm()
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

# Check list for adding data to the post Database:
# 1. Import Our Post Model - DONE
# 2. Instantiate the Post Model w/ the form data from PostForm - DONE
# 3. Create a Database Session for the Post Model -DONE
# 4. Add PostForm Data to the Post Model - DONE
# 5. Commit/Save the PostForm Data to the Post Model Database Table - DONE
@app.route('/post', methods=['GET','POST'])
@login_required
def post_blog():
    postForm = PostForm()
    if request.method == 'POST' and postForm.validate():
        title = postForm.title.data
        content = postForm.content.data
        user_id = current_user.id
        print(title,content,user)
        post = Post(title = title,content = content,user_id = user_id)

        # Add the PostForm Data to the Post Model 
        db.session.add(post)

        # Save/Commit PostForm Data to the Post Model Database Table
        db.session.commit()
        return redirect(url_for('post_blog'))
    else:
        flash('The information entered is not correct')
        print('Invalid data')
    return render_template('post-form.html', form = postForm)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post)

@app.route('/post/update/<int:post_id>',methods=['GET','POST'])
@login_required
def post_update(post_id):
    post = Post.query.get_or_404(post_id)

    # TODO Use PostForm for Update
    postForm = PostForm()
    if request.method == 'POST' and postForm.validate():
        title = postForm.title.data
        content = postForm.content.data
        user_id = current_user.id
        print(title,content,user_id)
        post.title = title
        post.content = content
        post.user_id = user_id

        db.session.commit()
        return redirect(url_for('home'))
    return render_template('post_update.html',form = postForm)

@app.route('/post/delete/<int:post_id>',methods=['POST'])
@login_required
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/user/<int:user_id>')
@login_required
def user_detail(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_detail.html', user = user)


# Update Route for User Information
@app.route('/user/update/<int:user_id>', methods=['GET','POST'])
@login_required
def user_update(user_id):
    user = User.query.get_or_404(user_id)

    userForm = UserInfoForm()
    if request.method == 'POST' and userForm.validate():
        username = userForm.username.data
        email = userForm.email.data
        password = userForm.password.data

        # Update User Info inside of the database
        user.username = username
        user.email = email
        user.password = user.set_password(password)

        db.session.commit()
        return redirect(url_for('home'))
    return render_template('user_update.html', form = userForm)


