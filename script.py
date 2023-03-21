import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import traceback
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def send_mail(receiver_email, spoofed_email, spoofed_name, message, subject):
    try:
        msg = MIMEMultipart("related")
        msg['From'] = f"{spoofed_name} <{spoofed_email}>"
        msg['To'] = receiver_email
        msg['Subject'] = subject
        body = message
        msg.attach(MIMEText(body, 'plain'))
        # Get SMTP settings from config file
        smtp_host = config.get('SMTP', 'host')
        smtp_port = config.getint('SMTP', 'port')
        smtp_username = config.get('SMTP', 'username')
        smtp_password = config.get('SMTP', 'password')
        # Connect to SMTP server and send email
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(spoofed_email, receiver_email, text)
        server.quit()
        print('Spoofed Email sent successfully to ' +
              str(receiver_email) + ' from ' + str(spoofed_name))
    except Exception as e:
        # Print the exception
        print(traceback.format_exc())


# Change the details below for spoofing
receiver_email = '<Receivers Email Address>'
spoofed_email = '<Spoofed Email Address>'
spoofed_name = '<Spoofed Name>'
message = '<Text Message to send>'
subject = '<Email Subject/Title>'

# Invoke send_mail to send email
send_mail(receiver_email, spoofed_email, spoofed_name, message, subject)
