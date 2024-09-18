from flask import Flask,Blueprint, render_template,request
from flask_login import login_required,current_user

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html',show_auth_buttons=True)

@main.route('/home')
def home():
    return render_template('index.html',show_auth_buttons=True)


@main.route('/mainpage/<username>')
def mainpage(username):
    return render_template('cards.html',show_auth_buttons=False,username=username)

@main.route('/calculator')
def calculator():
    return render_template('calculator.html')

@main.route('/modelpaper')
def modelpaper():
    return render_template('model_paper.html')