import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_email():
    fromaddr: str = 'mosiakoff80@mail.ru'
    toaddr = "mosiakoff80@mail.ru"
    mypass = "RSsBcmH489xYA4fm46XH"
    report_name = "log.txt"

    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg["To"] = toaddr
    msg["Subject"] = "Test stand report"

    with open(report_name, 'rb') as f:
        part = MIMEApplication(f.read(), Name=basename(report_name))
        part['Content-Disposition'] = 'attacment; filename=%s' % basename(report_name)
        msg.attach(part)

    body = "Test"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


if __name__ == '__main__':
    send_email()
