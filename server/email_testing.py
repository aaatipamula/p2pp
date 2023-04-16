#from datetime import datetime
#timestamp = datetime.now().strftime("%H_%M_%m_%d_%Y")
#print(timestamp)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
 
    # Authentication
    s.login('sparefoodforum@gmail.com', r'm%g*6pHabm3@hD$')
 
    # message to be sent
    message = "Testing123"
 
    # sending the mail
    s.sendmail("sender_email_id", "receiver_email_id", message)
    # terminating the session
    s.quit()

# Example usage:
smtp_port = 465 # Use the appropriate SMTP port for your email provider (e.g., 587 for TLS)
body = 'This is a test email sent using Python.'

send_email(sender_email)
