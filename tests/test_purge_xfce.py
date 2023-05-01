#!/usr/bin/env python3

"""
Name: test_purge_xfce.py
Purpose: test purge_xfce.py script

source: https://gitlab.com/kevinbowen/xfce-repocapp
version: 0.8.7
updated: 20230315
@author: kevin.bowen@gmail.com
"""

import unittest

from src import cappdata  # noqa: F401
from src.purge_xfce import purge_xfce  # noqa: F401

args = "bindings"


class TestPurgeXfce(unittest.TestCase):
    """Test the purge_xfce() function of purge_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print("setUp")
        pass

    def tearDown(self):
        """Tear down the test features."""
        print("tearDown\n")
        pass

    def test_purge_xfce(self):
        """testing purge_xfce() function."""
        pass


class TestMain(unittest.TestCase):
    """Test the main() function of purge_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print("setUp")
        pass

    def tearDown(self):
        """Tear down the test features."""
        print("tearDown\n")
        pass

    def test_main(self):
        """testing main() function in purge_xfce.py"""
        pass


if __name__ == "__main__":
    unittest.main()
