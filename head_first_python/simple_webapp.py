from flask import Flask, session
from checker import check_logged_in

app = Flask(__name__)
app.secret_key = "fuck_this_boring_app"

@app.route('/')
def hello() -> str:
    return "Hello from simple web app."


@app.route('/page1')
@check_logged_in
def page1() -> str:
    return "Page 1"


@app.route('/page2')
@check_logged_in
def page2() -> str:
    return "Page 2"


@app.route('/page3')
@check_logged_in
def page3() -> str:
    return "Page 3"


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return "Logged in."


@app.route('/logout')
def do_logout() -> str:
    session['logged_in'] = False
    return "Logged out."


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')











