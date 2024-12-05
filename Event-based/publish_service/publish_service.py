import pika
import smtplib
from email.mime.text import MIMEText

HOST = "smtp..."
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = "" # APP PASSWORD
ADDRESSEE = ""


def callback(message):
    message = message.decode()
    user, text = message.split("|", 1)
    print(f"Message received: {text}")

    to_email = ADDRESSEE
    message = MIMEText(text)
    message["Subject"] = "MESSAGE"
    message["From"] = EMAIL_ADDRESS
    message["To"] = to_email

    with smtplib.SMTP(HOST, 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, [to_email], message.as_string())

    print(f"Email sent for message: {text}")

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="PublishQueue")
channel.basic_consume(queue="PublishQueue", on_message_callback=callback, auto_ack=True)

print("Publish Service running...")
channel.start_consuming()
