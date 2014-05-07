

# Writing a test case

## Example test case

    from test_case import TestCase

    class FooLoadTest(TestCase):
        client_count = 10
        scenario = [
            'loadtest_signin',
        ]

        def echo(self):
            self.call_router('echo', 'echo-router')

Set the number of concurrent clients by settings ```client_count```.

Create functions to perform the tests

Specify the test functions to run by adding them to ```scenario```


# Running tests

```python run.py loadtest_foo```

