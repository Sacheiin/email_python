import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Curious man'
email['to'] = 'sacheein1999@gmail.com'
email['subject'] = 'You won a $1,000,000!'

email.set_content(html.substitute({'name': 'Robot'}))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('bcurious843@gmail.com', 'NAYNAY@12')
    smtp.send_message(email)
    print('all good boss!')
