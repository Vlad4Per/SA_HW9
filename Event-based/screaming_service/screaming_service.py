import pika


def callback(message):
    message = message.decode()
    user, text = message.split("|", 1)
    screaming_message = f"{user}|{text.upper()}"
    print(f"Message received: {text}")
    send_to_queue("PublishQueue", screaming_message)


def send_to_queue(queue, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange="", routing_key=queue, body=message)
    connection.close()


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="ScreamingQueue")
channel.basic_consume(queue="ScreamingQueue", on_message_callback=callback, auto_ack=True)

print("Screaming Service running...")
channel.start_consuming()
