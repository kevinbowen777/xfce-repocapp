#!/usr/bin/env python3

"""
Name: test_pull_xfce.py
Purpose: test pull_xfce.py script

source: https://gitlab.com/kevinbowen/xfce-repocapp
version: 0.8.7
updated: 20230315
@author: kevin.bowen@gmail.com
"""

import unittest

from cappdata import component_list  # noqa: F401
from pull_xfce import pull_xfce  # noqa: F401

args = "bindings"


class TestPullXfce(unittest.TestCase):
    """Test the pull_xfce() function of pull_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print("setUp")
        pass

    def tearDown(self):
        """Tear down the test features."""
        print("tearDown\n")
        pass

    def test_pull_xfce(self):
        """testing pull_xfce() function."""
        pass


class TestMain(unittest.TestCase):
    """Test the main() function of pull_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print("setUp")
        pass

    def tearDown(self):
        """Tear down the test features."""
        print("tearDown\n")
        pass

    def test_main(self):
        """testing main() function in pull_xfce.py"""
        pass


if __name__ == "__main__":
    unittest.main()
