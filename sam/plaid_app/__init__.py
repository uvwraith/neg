from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.secret_key = "edeacda59ac156398eb419c6b1ba496a5b8d0250cbf6f09299"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'Normanday26@gmail.com'
app.config['MAIL_PASSWORD'] = 'yqmadwvxwgvqphdy' #os.environ.get('MAIL_PASSWORD')

mail = Mail(app)

from plaid_app.main.routes import main
from plaid_app.portals.routes import portals

app.register_blueprint(main)
app.register_blueprint(portals)