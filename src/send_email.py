from dotenv import load_dotenv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl 
import configparser



config = configparser.ConfigParser()
config.read('config.ini')


port = 465
receiving_email = os.getenv('RECEIVING_EMAIL')
sending_email = os.getenv('SENDING_EMAIL')
password = os.getenv('EMAIL_PASSWORD')


message = MIMEMultipart("alternative")
message["Subject"] = "There's a Sale!"
message["From"] = sending_email
message["To"] = receiving_email
html = """\
<html>
  <body>
    <p>
        That item you were looking at is finally on sale! <br>
        Have a look here: <a href="#">Link</a> 
    </p>
  </body>
</html>
"""
message.attach(MIMEText(html, "html"))


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sending_email, password)
    server.sendmail(
        sending_email, receiving_email, message.as_string()
    )