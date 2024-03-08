from flask import Blueprint, render_template, request, redirect, url_for, jsonify
# Stub code for authorisation functions

user_details = Blueprint('user_details', __name__)


# Returns user details based on userId input, includes name, email, password, dateRegistered.
@user_details.route('/details', methods=['GET'])
def userDetails():
        user_id = request.args.get('user_id')
        return 'user_info' # stub return



# Updates and returns email for given user through userId and old email. Returns error message if update fails.
@user_details.route('/email', methods=['GET'])
def updateEmail():
    user_id = request.args.get('user_id')
    email = request.form['email']
    return email

# Updates and returns password for given user through userId and old password. Returns error message if update fails.
@user_details.route('/password', methods=['GET'])
def updatePassword():
    user_id = request.args.get('user_id')
    password = request.form['passowrd']
    confirm_password = request.form['confirmPassword']
    return password

# Logs registered user out and redirects them to login/signup page.
@user_details.route('/logout', methods=['GET'])
def userLogout():
    user_id = request.args.get('user_id')
    return None