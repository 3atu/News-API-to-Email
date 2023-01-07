import smtplib
import ssl
import os


def send_email(message):

    host = "smtp.gmail.com"
    port = 465

    username = "batuhofer@gmail.com"
    password = os.getenv("PASSWORD") # Password is stored in user OS

    receiver = "batuhofer@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)