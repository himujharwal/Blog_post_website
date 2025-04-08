from flask import Flask, render_template, request,jsonify, redirect, url_for, session, flash, get_flashed_messages
# from markupsafe import escape
from form import RegistrationForm, LoginForm
# print("hellow world")


app = Flask(__name__)

app.config['SECRET_KEY']= '15644274b06634631ae8cf766cfd6167'



posts = [
    { 
        'author':'himanshu',
         'age': 24,
         'post':'first post of my about the jinja templates'

    }, 
    { 
    'author':'kushal',
        'age': 23,
        'post':'second post about the frondetend developmendts'

    }
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'about title')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm() 
    if form.validate_on_submit():
        flash('Accound has been {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registration Form', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'himujharwal@gmail.com' and form.password.data=='password':
            flash("you have been logged in", 'success')
            return redirect(url_for('home'))
        else:
            flash("unsuccesfull log in. you need email and password", 'danger')
    return render_template('login.html', title = 'LoginForm', form=form)














'''porject 2 ==> just returninh the get and post method based json file , validation'''


# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/hello/<name>')
# def hello(name):
#     return render_template('hello.html', username=name)

# @app.route('/data', methods=['POST'])
# def data():
#     data = request.get_json()
#     if not data or not 'username' in data:
#         return f"404 no found error"
#     else:
#         return jsonify({
#             'message':"recieved data",
#             'your_data': data
#                      })


# @app.route('/search')
# def search():
#     item = request.args.get('item')
#     price = request.args.get('price')
#     return f"product{item}:{price}"

# @app.route('/feedback', methods = ['GET', 'POST'])
# def feedback():
#     if request.method == 'GET':
#         return render_template('feedback_form')
#     else :
#         name = request.form.get('name')
#         message = request.form.get('message')

#         if not name or not message :
#             error = "both name and message required"
#             return render_template('feedback_form.html', error = error)
        
#         return render_template('feedback_result', name = name , message = message)


'''project 3 ==> login page with session and flash'''

# app.secret_key = 'mykey123'


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         return render_template('login_form.html')
#     else:
#         session['username'] = request.form.get('username')
#         flash("You are logged in successfully")
#         return redirect(url_for('profile'))

# @app.route('/profile')
# def profile():
#     username = session.get('username')
#     if username:
#         return f"Welcome Mr. {username}"
#     else:
#         flash("You need to login first")
#         return redirect(url_for('login'))

# @app.route('/logout')
# def logout():
#     session.clear()
#     flash("Logged out successfully")
#     return redirect(url_for('login'))


# @app.route('/user/<username>')
# def user(username):
#     return f'Hi there , i guess you user name is "{escape(username)}"' 

if __name__== "__main__":
    app.run(debug=True)

