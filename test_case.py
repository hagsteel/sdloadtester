# from tornado.ioloop import IOLoop
from connections.connection import DragonClient
# import threading


class TestCase(object):
    client_count = 1
    clients = []
    _thread = None
    call_count = 0
    scenario = []

    def __init__(self):
        for i in range(self.client_count):
            client = DragonClient('ws://localhost:9999/data')
            self.clients.append(client)

            client.connect()
            client.run()
            # self._thread = threading.Thread(target=client.run)
            # self._thread.start()

    def call_router(self, verb, route, **kwargs):
        for c in self.clients:
            c.call_router(verb, route, **kwargs)
            self.call_count += 1
        print(self.call_count)
