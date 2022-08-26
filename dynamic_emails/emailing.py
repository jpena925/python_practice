#outdated email sending

#simple mail transfer protocol library
import smtplib

from email.message import EmailMessage
from string import Template
from pathlib import Path #similar to os.path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Jack Pena'
email['to'] = 'dummyemail@gmail.com'
email['subject'] = 'Dummy subject line'

#here you can set the name variable that is in index.html 
email.set_content(html.substitute(name='TinTin') , 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('myemail@gmail.com', 'mypassword')
    smtp.send_message(email)
    print('email sent!')
