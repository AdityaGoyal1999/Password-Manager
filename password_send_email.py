""" This python class is to send email to the user who has forgotten his
password."""
import smtplib
from email.message import EmailMessage


def send_email(email: str, password: str, _content: str) -> None:
    """ sends the recovery email to the user.

    The email login is encrypted.
    Precondition: this functionality is only available to the gmail users
    """
    content = EmailMessage()
    content.set_content(_content)
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.starttls()
    mail.login(email, password)
    mail.send_message(content, email, email)
    mail.close()
