import asyncio
import inspect
# from tornado.ioloop import IOLoop
from test_case import TestCase


def load_tests(test_class):
    test_classes = []
    try:
        test_case_module = __import__('testcases.{}'.format(test_class), fromlist=["testcases"])
        classes = inspect.getmembers(test_case_module, inspect.isclass)
        for c in classes:
            if c[1].__base__ == TestCase:
               test_classes.append(c[1])
    except ImportError:
        pass
    return test_classes


def run_tests(tests):
    # ioloop = IOLoop.current()

    for test in tests:
        instance = test()
        for f in instance.scenario:
            getattr(instance, f)()

    loop = asyncio.get_event_loop()
    loop.run_forever()
    print('got here')
    # ioloop.start()