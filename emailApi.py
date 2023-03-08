import csv
from email.message import EmailMessage
import os
import smtplib
from email.mime.text import MIMEText
import time

def send_email(subject, body, sender, link, recipients, password, k):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = [mail]
    msg.set_content(f'''
    <!DOCTYPE html>
    <html>
        <body>
            <div style="padding:20px 0px">
                <div style="height: 500px;width:400px">
                    <img src="https://i.imgur.com/ujTCJ20.png" style="width: 100px;">
                    <div style="text-align:center;">
                        <h3>{subject}</h3>
                        <p>{body}</p>
                        <a href="{link}">Read more...</a>
                        <small>Message sent via temporary email address.</small>
                    </div>
                </div>
            </div>
        </body>
    </html>
    ''', subtype='html')
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()

def get_lines(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return lines

filename = open('members.csv', 'r') 
file = csv.DictReader(filename)
emails = []

for col in file:
    emails.append(col['email'])


subject = "OSUT te informeaza - Concurs cea mai buna grupa"
body = """
    Concursul pentru cea mai bună grupă este în desfășurare. Dacă dorești să fii răsplătit pentru munca depusă în sesiune și notele bune pe care le-ai obținut, nu mai sta pe gânduri și înscrie-te împreună cu colegii tăi din grupă în competiție. Aveți șansa de a câștiga o excursie în țară sau în străinătate. 
Reamintim că validarea înscrierii se face prin dovada evaluării cadrelor didactice a minimum 60% din colectiv.
"""
link = "https://osut.org/concurs-cea-mai-buna/"

sender = "itosutcj@gmail.com"
recipients = emails.reverse()
password = os.environ["secrets-osutBot"]

k = 0
for mail in emails:
    try:
        send_email(subject, body, sender, link, mail, password, k)
        print(f"Succes sending email to {mail}")
    except:
        print(f"Failed to send email to {mail}")
    k += 1
    time.sleep(2)