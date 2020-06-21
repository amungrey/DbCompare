import os
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import datetime
from os.path import basename

DEFAULT_PDS_RECIPIENTS = []

def send_mail(body,html_body, recipients, file_list=[]):
    try:
        username = os.getlogin()
    except OSError:
        import pwd
        username=pwd.getpwuid(os.geteuid())[0]
    sender = username
    timestamp = str(datetime.datetime.now())
    msg = MIMEMultipart
    if html_body:
        body = body.replace('\n', '<br')
        body = body.replace('\t', '&#9;')
        html_body = body + html_body
        msg.attach(MIMEText(html_body, 'html'))
    else:
        msg.attach(MIMEText(body,'plain'))

    if file_list:
        for file in file_list:
            with open(file, "rb") as f:
                part = MIMEApplication(f.read(), Name=basename(file))
            part['Content-Disposition'] ='attachment;filename ="%s"' %os.path.basename(file)
            msg.attach(part)

    msg['From']=sender
    msg['To'] =', '.join(recipients)
    msg['Subject']=' '.join(['DBCompare'],timestamp)

    server = smtplib.SMTP('localhost')
    server.sendmail(sender,recipients,msg.as_string())
    server.quit()
