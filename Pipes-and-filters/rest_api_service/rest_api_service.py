from flask import Flask, request, jsonify


def rest_api_service(queue):
    app = Flask(__name__)

    @app.route('/send', methods=['POST'])
    def send_message():
        # Check the format of a message and send it to filter
        if 'message' not in request.json or 'user' not in request.json: return jsonify(
            {"error": "Invalid request"}), 400
        message = f"{request.json['user']}|{request.json['message']}"
        queue.put(message)
        return jsonify({"status": "Message sent successfully"}), 200

    app.run(port=5001)
