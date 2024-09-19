from flask import Flask,Blueprint, render_template,request
from flask_login import login_required,current_user
import requests 

main = Blueprint('main',__name__)

@main.route('/')
def index():
        response=requests.get('https://api.kanye.rest/')
        if response.status_code == 200:
            data = response.json()
            quote = data['quote']
        return render_template('index.html',show_auth_buttons=True,quote=quote)

@main.route('/home')
def home():
        response=requests.get('https://api.kanye.rest/')
        if response.status_code == 200:
            data = response.json()
            quote = data['quote']
        return render_template('index.html',show_auth_buttons=True,quote=quote)

@main.route('/mainpage/<username>')
def mainpage(username):
    return render_template('cards.html',show_auth_buttons=False,username=username)

@main.route('/calculator')
def calculator():
    return render_template('calculator.html')

@main.route('/modelpaper')
def modelpaper():
    return render_template('model_paper.html')







