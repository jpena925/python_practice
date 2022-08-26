#outdated email sending

#simple mail transfer protocol library
import smtplib

from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Jack Pena'
email['to'] = 'dummyemail@gmail.com'
email['subject'] = 'Dummy subject line'

email.set_content('Content goes here')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('myemail@gmail.com', 'mypassword')
    smtp.send_message(email)
    print('email sent!')
