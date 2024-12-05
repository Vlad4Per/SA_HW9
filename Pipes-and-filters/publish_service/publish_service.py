import smtplib
from email.mime.text import MIMEText

# from
EMAIL_ADDRESS = "your_email_address"
APP_PASSWORD = "your_password"

# to
ADDRESSEE = EMAIL_ADDRESS

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

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, APP_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, [ADDRESSEE], message.as_string())

        print(f"Email sent for message: {text}")
