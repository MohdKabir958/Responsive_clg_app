from pragnya_responsive_app import create_app
import os 
from flask_login import LoginManager


app = create_app()


UPLOAD_FOLDER = 'uploads'  # Make sure this folder exists
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__=="__main__":
    app.run(debug=True)

    


