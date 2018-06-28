from flask import Flask, session

app = Flask(__name__)
app.secret_key = "fuck_this_boring_app"

@app.route('/')
def hello() -> str:
    return "Hello from simple web app."


@app.route('/page1')
def page1() -> str:
    return "Page 1"


@app.route('/page2')
def page2() -> str:
    return "Page 2"


@app.route('/page3')
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


@app.route('/status')
def check_status() -> str:
    if session['logged_in'] == True:
        return "Status OK"
    return "Not authorized"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')











