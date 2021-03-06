"""Run all tests.

Author: Matthew Harrigan
"""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future.builtins import *
import unittest
import argparse

from pkg_resources import resource_filename


def parse():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action='count', default=1)
    args = parser.parse_args()
    main(args.verbose)


def main(verbosity=1):
    """Discover and run tests."""
    runner = unittest.TextTestRunner(verbosity=verbosity)
    suite = unittest.defaultTestLoader.discover(
        resource_filename('wetmsm', 'testing/'))
    runner.run(suite)


if __name__ == "__main__":
    parse()
