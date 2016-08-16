from demo.celery import app
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

@app.task
def hello_world():
    print('Hello World,fvf')

@app.task
def sendEmail():
    fromaddr = "simba_cc@163.com"
    toaddr = "287517825@qq.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "SUBJECT OF THE MAIL"

    body = "YOUR MESSAGE HERE"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.163.com',25)
    server.starttls()
    server.login(fromaddr, "******")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    return
