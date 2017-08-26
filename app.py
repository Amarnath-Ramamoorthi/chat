from flask import Flask, render_template, json, request
from werkzeug import generate_password_hash, check_password_hash
import csv
# import logging as log

global users_file
print('START')
users_file = 'users.csv'

app = Flask(__name__)

# class User(object):

#     def __init__(self, username, password):
#         self.username = username
#         self.set_password(password)

#     def set_password(self, password):
#         self.pw_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.pw_hash, password)

@app.route("/")
def main():
    return render_template('login.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/login',methods=['POST'])
def login():
 
    # read the posted values from the UI
    _name = request.form['inputName']
    _password = request.form['inputPassword']
    # _hashed_password = generate_password_hash(_password)
    # user = User(_name,_password)
    # user.set_password(_password)

	# validate the received values
    if (_name and _password):
    	with open(users_file) as csvfile:
			users = csv.DictReader(csvfile)
			for row in users:
				# print(row['name'], row['password'])
				if (_name == row['name']) and (_password == row['password']):
					return json.dumps({'html':'Login Success', 'name': _name})
	   	    	else:
					return json.dumps({'html':'Login Failed'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


@app.route('/signup',methods=['POST'])
def signup():
 
    # read the posted values from the UI
    _name = request.form['inputName']
    _password = request.form['inputPassword']

	# validate the received values
    if _name and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

    with open(users_file,'a',newline='') as f:
    	writer=csv.writer(f)
    	writer.writerow([_name, '', _password, 0])

    # _hashed_password = generate_password_hash(_password)    

if __name__ == "__main__":
    app.run()




