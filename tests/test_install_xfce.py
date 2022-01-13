#!/usr/bin/env python3

"""
Name: test_install_xfce.py
Purpose: test install_xfce.py script

source: https://gitlab.com/kevinbowen/xfce-repocapp
version: 0.8.5
updated: 20220112
@author: kevin.bowen@gmail.com
"""

import unittest

from install_xfce import install_xfce
from install_xfce import main


class TestInstallXfce(unittest.TestCase):
    """Test the install_xfce() function of install_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print('setUp')
        pass

    def tearDown(self):
        """Tear down the test features."""
        print('tearDown\n')
        pass

    def test_install_xfce(self):
        """testing install_xfce() function"""
        pass


class TestMain(unittest.TestCase):
    """Test the main() function of install_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print('setUp')
        pass

    def tearDown(self):
        """Tear down the test features."""
        print('tearDown\n')
        pass

    def test_main(self):
        """testing main() function in install_xfce.py"""
        pass


if __name__ == '__main__':
    unittest.main()
