def screaming_service(input_queue, output_queue):
    while True:
        # Change all symbols to uppercase and send to publish service
        message = input_queue.get()
        if message is None: break
        user, text = message.split('|', 1)
        text = text.upper()
        message = f"{user}|{text}"
        output_queue.put(message)
