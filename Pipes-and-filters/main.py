from multiprocessing import Process, Queue
from rest_api_service import rest_api_service
from filter_service import filter_service
from screaming_service import screaming_service
from publish_service import publish_service

if __name__ == '__main__':
    # creating queues
    filter_q = Queue()
    screaming_q = Queue()
    publish_q = Queue()

    # creating processes
    rest_api = Process(target=rest_api_service, args=(filter_q,))
    filter = Process(target=filter_service, args=(filter_q, screaming_q))
    screaming = Process(target=screaming_service, args=(screaming_q, publish_q))
    publish = Process(target=publish_service, args=(publish_q,))

    # starting processes
    rest_api.start()
    filter.start()
    screaming.start()
    publish.start()

    # finishing processes
    rest_api.join()
    filter.join()
    screaming.join()
    publish.join()
