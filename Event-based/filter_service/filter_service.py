import pika


def callback(channel, method, properties, body):
    message = body.decode()
    user, text = message.split("|", 1)

    if "bird-watching" in text or "ailurophobia" in text or "mango" in text:
        print(f"Message dropped due to stop-word: {text}")
    else:
        print(f"Message received: {text}")
        send_to_queue("ScreamingQueue", message)


def send_to_queue(queue, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange="", routing_key=queue, body=message)
    connection.close()


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="FilterQueue")
channel.basic_consume(queue="FilterQueue", on_message_callback=callback, auto_ack=True)

print("Filter Service running...")
channel.start_consuming()
