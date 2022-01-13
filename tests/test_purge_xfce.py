#!/usr/bin/env python3

"""
Name: test_purge_xfce.py
Purpose: test purge_xfce.py script

source: https://gitlab.com/kevinbowen/xfce-repocapp
version: 0.8.5
updated: 20220112
@author: kevin.bowen@gmail.com
"""

import unittest

from purge_xfce import purge_xfce
from purge_xfce import main


class TestPurgeXfce(unittest.TestCase):
    """Test the purge_xfce() function of purge_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print('setUp')
        pass

    def tearDown(self):
        """Tear down the test features."""
        print('tearDown\n')
        pass

    def test_purge_xfce(self):
        """testing purge_xfce() function."""
        pass


class TestMain(unittest.TestCase):
    """Test the main() function of purge_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print('setUp')
        pass

    def tearDown(self):
        """Tear down the test features."""
        print('tearDown\n')
        pass

    def test_main(self):
        """testing main() function in purge_xfce.py"""
        pass

if __name__ == '__main__':
    unittest.main()
