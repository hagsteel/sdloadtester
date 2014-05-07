import asyncio
import random
import string
import websocket
import threading
import json


def message_to_json(data):
    if isinstance(data, dict):
        return data
    try:
        data = json.loads(data)
        data = json.loads(data)
        return data
    except:
        return json.dumps({'message': data})


class DragonClient(object):
    def __init__(self, url):
        if url[-1] != '/':
            url = '{}/'.format(url)
        self.url = '{}{}/{}/websocket'.format(url, self._rand_int(), self._rand_string())
        self.call_queue = []
        self.is_connected = False

    def _rand_int(self):
        return random.randint(0, 1000)

    def _rand_string(self):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

    def connect(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )

    def on_message(self, ws, message):
        if message[0:2] == 'a[' or message[0] == 'm':
            pass
            # print('-- msg --')
            # message = message_to_json(message)
            # print(message)

    def on_error(self, ws, error):
        print('-- err --')
        print(error)

    def on_close(self, ws):
        self.is_connected = False

    def on_open(self, ws):
        self.is_connected = True
        for f in self.call_queue:
            self._send(f)

    def _send(self, message):
        self.ws.send(message)

    @asyncio.coroutine
    def run(self):
        self.ws.run_forever()

    def call_router(self, verb, route, **kwargs):
        message = json.dumps({
            'verb': verb,
            'route': route,
            'args': kwargs
        })

        if self.is_connected:
            self._send(message)
        else:
            self.call_queue.append(message)


def do_stuff(prefix, host, port):
    url = 'ws://localhost:9999/data'
    client = DragonClient(url)
    client.connect()
    t = threading.Thread(target=client.run)
    t.start()

    ipt = input('Cho: ')
    while ipt != 'q':
        if ipt == 'l':
            client.call_router('signin', 'accounts', username='test', password='test')
        ipt = input('Cho: ')
