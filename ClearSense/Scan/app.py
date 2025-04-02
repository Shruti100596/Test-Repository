from flask import Flask, request, render_template_string
from login_new1_club import run_login_club
from forgot_password import run_forgot_password
from signup_club_new import run_signup1
from logout_club import run_logout
from create_offer_club import run_createoffer_club
from add_affiliate_club import run_add_affiliate
from add_new_affiliate_club import run_add_new_affiliate
from edit_offer_club import run_edit_offer
from create_adjust_offer_club import  run_create_adjustoffer_club
from Create_Link_Offer import run_create_links_club

app = Flask(__name__)

@app.route('/run-login_new1_club')
def run_my_login_club():
    result = run_login_club()
    return result

@app.route('/run-forgot_password')
def run_my_forgot_password():
    result = run_forgot_password()
    return result


@app.route('/')
def index():
    # Use render_template to serve the HTML file
    return render_template('main1.html')


@app.route('/run-signup_club_new')
def run_my_signup_club():
    result = run_signup1()
    return result  # Return the result of the signup process

@app.route('/run-logout_club')
def run_my_logout_club():
    result = run_logout()
    return result


@app.route('/run-create_offer_club')
def run_my_createoffer_club():
    result = run_createoffer_club()
    return result

@app.route('/run-add_affiliate_club')
def run_my_add_affiliate_club():
    print("app.py file")
    result = run_add_affiliate()
    return result

@app.route('/run-add_new_affiliate_club')
def run_my_add_new_affiliate():
    print("app.py file")
    result = run_add_new_affiliate()
    return result    


@app.route('/run-edit_offer_club')
def run_my_editoffer_club():
    result = run_edit_offer()
    return result

@app.route('/run-create_adjust_offer_club')
def run_my_creatadjustoffer_club():
    result = run_create_adjustoffer_club()
    return result

@app.route('/run-Create_Link_Offer')
def run_my_create_links_club():
    result = run_create_links_club()
    return result

if __name__ == '__main__':
    app.run(debug=True)









