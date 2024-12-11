import smtplib,ssl
from dotenv import load_dotenv
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD_FOR_COMPANY")
    print(password)

    receiver = "soolotus632@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

