#!/usr/bin/env python3

"""
Name: test_clean_xfce.py
Purpose: test clean_xfce.py script

source: https://gitlab.com/kevinbowen/xfce-repocapp
version: 0.8.6
updated: 20220113
@author: kevin.bowen@gmail.com
"""

import unittest


class TestCleanXfce(unittest.TestCase):
    """Test the clone_xfce() function of clone_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print('setUp')
        pass

    def tearDown(self):
        """Tear down the test features."""
        print('tearDown\n')
        pass

    def test_clean_xfce(self):
        """testing clean_xfce() function."""
        pass


class TestMain(unittest.TestCase):
    """Test the main() function of clean_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print('setUp')
        pass

    def tearDown(self):
        """Tear down the test features."""
        print('tearDown\n')
        pass

    def test_main(self):
        """testing main() function in clean_xfce.py"""
        pass


if __name__ == '__main__':
    unittest.main()
