import smtplib
from email.mime.text import MIMEText
import time

# from
HOST = "" # Your HOST, e. g. smtp.bk.ru
EMAIL_ADDRESS = "example@mail.com" # Your email
APP_PASSWORD = "passwd" # Your password

# to
ADDRESSEE = EMAIL_ADDRESS # Selfdirected letter

def publish_service(input_queue):
    # Send the message (with no stop-words and uppercase) to addressee from addresser
    while True:
        message = input_queue.get()
        if message is None:
            break
        user, text = message.split('|', 1)

        message = MIMEText(text)
        message['Subject'] = f"Message from {user}"
        message['From'] = EMAIL_ADDRESS
        message['To'] = EMAIL_ADDRESS

        with smtplib.SMTP(HOST, 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, APP_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, [ADDRESSEE], message.as_string())

        print(f"Email sent for message: {text}")
        print(f"Time (end): {time.time()}\n")
