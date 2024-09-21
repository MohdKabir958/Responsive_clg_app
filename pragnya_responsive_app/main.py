from flask import Flask,Blueprint, render_template,request,current_app,send_from_directory
from flask_login import login_required,current_user
import requests 
import os 
from werkzeug.utils import secure_filename
import uuid

main = Blueprint('main',__name__)

@main.route('/')
def index():
        response=requests.get('https://api.kanye.rest/')
        if response.status_code == 200:
            data = response.json()
            quote = data['quote']
        show_auth_buttons = not current_user.is_authenticated
        return render_template('index.html',show_auth_buttons=show_auth_buttons,quote=quote)

@main.route('/home')
def home():
        response=requests.get('https://api.kanye.rest/')
        if response.status_code == 200:
            data = response.json()
            quote = data['quote']
        show_auth_buttons = not current_user.is_authenticated
        return render_template('index.html',show_auth_buttons=show_auth_buttons,quote=quote)

@main.route('/mainpage/<username>')
@login_required
def mainpage(username):
    return render_template('cards.html',show_auth_buttons=False,username=username)

@main.route('/calculator')
def calculator():
    return render_template('calculator.html')

@main.route('/modelpaper')
def modelpaper():
    return render_template('model_paper.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('cards.html', username=current_user.name)



@main.route('/process_data', methods=['POST'])
def process_data():
    my_js_var = request.form['my_js_var']  # Access the JavaScript variable from the form
    print(f"Received data from JavaScript: {my_js_var}")
    return f"Received: {my_js_var}"

@main.route('/account')
@login_required
def account():
    user_details = {
        'id': current_user.id,
        'username': current_user.name,
        'email': current_user.email,
        # Add other attributes as needed
    }
    return render_template('accounts.html', user=user_details)


@main.route('/upload', methods=['POST'])
def upload_file():
    if 'profile_pic' not in request.files:
        return "No file part"
    
    file = request.files['profile_pic']
    
    if file.filename == '':
        return "No selected file"
    
    # Ensure the uploads directory exists
    upload_folder = current_app.config.get('UPLOAD_FOLDER', 'uploads')
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    # Secure the filename
    filename = secure_filename(file.filename)
    file_path = os.path.join(upload_folder, filename)
    
    # Handle potential filename conflicts by renaming
    if os.path.exists(file_path):
        # filename = f"{str(uuid.uuid4())}_{filename}"
        file_path = os.path.join(upload_folder, filename)
    
    # Save the file
    file.save(file_path)
    print("Upload folder:", upload_folder)
    print("Saved file path:", file_path)

    # Render the template to display the uploaded image
    return render_template('accounts.html', filename=filename)


@main.route('/uploads/<filename>', methods=['GET', 'POST'])
def display_image(filename):
    
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)
