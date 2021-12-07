from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from jinja2 import Template
from threading import Thread
import smtplib

from config import env

# List of templates 'filename' : 'Header of template'
subjects = {
    'reset-password' : 'Reset password',
    'confirm-email' : 'Confirm your email',
}

class Email:

    def __init__(self) -> None:
        try:
            self.smtp = smtplib.SMTP_SSL(env('MAIL_HOST'), env('MAIL_PORT'))
            self.smtp.login(env('MAIL_USERNAME'), env('MAIL_PASSWORD'))
            print ("Email works!")
        except Exception as e:
            print (f"Email error: {e}")


        
    def send(self, layout : str, receiver : dict, data : dict = {}) -> None:
        
        email_sending = Thread(target=self.__sending, args=(layout, receiver, data))
        email_sending.start()
        
        
    def __sending(self, layout, receiver, data) -> None:

        try:
            message = MIMEMultipart('related')
            message['Subject'] = subjects[layout]
            message['From'] = str(Header(f"{env('MAIL_FROM_NAME')} <{env('MAIL_FROM_ADDRESS')}>")) 

            with open(f'./emails/{layout}.html.jinja2') as file:

                template = Template(file.read())
                html = template.render(data=data)
                message.attach(MIMEText(html, "html"))

            self.smtp.sendmail(env('MAIL_FROM_ADDRESS'), receiver['email'], message.as_string())
            print ("Successfully sent email")
        except Exception as e:
            print (f"Error: unable to send email {e}")



    def __del__(self):
        self.smtp.close()
