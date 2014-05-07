#!/usr/bin/env python
import sys
import test_runner


if __name__ == '__main__':
    tests = []
    if len(sys.argv) > 1:
        selected_tests = sys.argv[1:]
    for tc in selected_tests:
        loaded_tests = test_runner.load_tests(tc)
        if loaded_tests:
            tests += loaded_tests

    test_runner.run_tests(tests)
