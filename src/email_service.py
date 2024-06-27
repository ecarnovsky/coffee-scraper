from dotenv import load_dotenv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl 
import configparser


class EmailService:

  
  def __init__(self):
     
    config = configparser.ConfigParser()
    config.read('config.ini')

    self.port = 465
    self.receiving_email = os.getenv('RECEIVING_EMAIL')
    self.sending_email = os.getenv('SENDING_EMAIL')
    self.password = os.getenv('EMAIL_PASSWORD')


  def send_email(self, sale_items):

    message = MIMEMultipart("alternative")
    message["Subject"] = "There's a Sale!"
    message["From"] = self.sending_email
    message["To"] = self.receiving_email
    sale_item_str = ""
    for item in sale_items:
       sale_item_str += f"""<br><li>
        <a href=\"{item.url}\">{item.name}</a>: Original Price: {item.original_price}, Sale Price: {item.sale_price}
       </li>"""
    html = f"""\
    <html>
      <body>
        <p>
            The following item(s) are on sale: <br>
            <ul>
              {sale_item_str}
            </ul> 
        </p>
      </body>
    </html>
    """
    message.attach(MIMEText(html, "html"))


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context) as server:
        server.login(self.sending_email, self.password)
        server.sendmail(
            self.sending_email, self.receiving_email, message.as_string()
        )