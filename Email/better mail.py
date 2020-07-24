import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html=Template(Path('index.html').read_text())
email=EmailMessage()
email['from']='Akash Hegde'
email['to']='imvinayak19@gmail.com'
email['subject']='you won a 1,000,000 dollars!'
# email.set_content('I am a python Master!')
email.set_content(html.substitute({'name':'Akash'}),'html')


with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('akashhegde2012@gmail.com','8618302335')
    smtp.send_message(email)
    print('all good boss')