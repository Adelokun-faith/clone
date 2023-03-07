from flask import Flask, redirect, url_for, request
from flask.templating import render_template


app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    # error = None
    # if request.method == 'POST':
    #     if request.form['username'] != 'user' or request.form['password'] != 'user':
    #         error = 'Invalid Credentials. Please try again.'
    #     else:
    #         return redirect(url_for('home'))
    return render_template('login.html')



if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0')
