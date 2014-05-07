from test_case import TestCase


class SigninLoadTest(TestCase):
    client_count = 2
    scenario = [
        'signin',
        'get_pages',
    ]

    def signin(self):
        self.call_router('signin', 'accounts', username='test', password='test')

    def get_pages(self):
        self.call_router('get_list', 'pages')
