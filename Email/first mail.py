import smtplib
from email.message import EmailMessage
email=EmailMessage()
email['from']='Akash Hegde'
email['to']='akashhegde2018@gmail.com'
email['subject']='you won a 1,000,000 dollars!'
email.set_content('I am a python Master!')


with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('akashhegde2012@gmail.com','8618302335')
    smtp.send_message(email)
    print('all good boss')