STOP_WORDS = {'bird-watching', 'ailurophobia', 'mango'}


def filter_service(input_queue, output_queue):
    while True:
        # Check the existence of stop-words and send to screaming service
        message = input_queue.get()
        if message is None: break
        user, text = message.split('|', 1)
        for word in STOP_WORDS:
            if word in text:
                print(f"Stop-word found: {text}")
                break
        else:
            output_queue.put(message)
