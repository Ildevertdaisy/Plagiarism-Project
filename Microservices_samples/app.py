from flask import Flask
from flask_mail import Mail, Message
import os


app = Flask(__name__)


app.config['MAIL_SERVER'] = 'live.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'api'
app.config['MAIL_PASSWORD'] = '15389d83d7d4c398ddedcdb53065e9f5'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False


mail = Mail(app)


@app.route("/send")
def send():
    message = Message(
        subject='Hello from other side!',
        recipients=['ildevertdaisy@gmail.com'],
        sender='robot@cherlock-ai.com'
    )

    message.body = "Hey Ildo, how are you."
    #message.html = "<p>Hello</p>"
    mail.send(message)

    return "Message sent!"