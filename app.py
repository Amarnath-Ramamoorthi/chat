from flask import Flask, render_template, json, request
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('login.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signup',methods=['POST'])
def signup():
 
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

	# validate the received values
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

    _hashed_password = generate_password_hash(_password)    


if __name__ == "__main__":
    app.run()



