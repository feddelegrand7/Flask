from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] ='11c3642bb25fdb2a010a75d1ed7e2bce'

posts = [

    {
        'author': 'Ihaddade Fodil',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2020'
    },

{
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2020'
    },



]

@app.route('/')
def hello_world():
    return render_template('home.html', posts=posts)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)




if __name__ == '__main__':
    app.run()
