from flask import Flask, request, jsonify
import pika

app = Flask(__name__)

def send_to_queue(queue, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange="", routing_key=queue, body=message)
    connection.close()

@app.route("/send", methods=["POST"])
def send_message():
    data = request.json

    if "message" not in data or "user" not in data:
        return jsonify({"error": "Invalid data"}), 400

    message = f"{data["user"]}|{data["message"]}"
    send_to_queue("FilterQueue", message)
    return jsonify({"status": "Message sent to FilterQueue"}), 200

if __name__ == "__main__":
    app.run(port=5000)
