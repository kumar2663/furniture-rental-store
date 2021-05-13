from flask_mail import Mail, Message

mail = Mail()


def send_email(sender,to, subject, template):
    msg = Message(subject,
                  html=template,
                  recipients=[to],
                  sender=sender)
    mail.send(msg)
