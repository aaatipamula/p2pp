from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(recipient_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = 'sparefoodforum@gmail.com'
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.ehlo()
            server.login('sparefoodforum@gmail.com', r'igngtfhbqwgijcde')
            server.sendmail('sparefoodforum@gmail.com', recipient_email, msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print("Error occurred while sending email:", e)

def get_time():
    return datetime.now().strftime("%H_%M_%m_%d_%Y")

if __name__ == '__main__':
    timestamp = datetime.now().strftime("%H_%M_%m_%d_%Y")
    recipient_email = 'arnavjain20042@gmail.com'
    subject = 'Second Test Email'
    body = 'This is a test email sent using Python. It was sent at ' + timestamp
    send_email(recipient_email, subject, body)
