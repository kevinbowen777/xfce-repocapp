#!/usr/bin/env python3

"""
Name: test_build_xfce.py
Purpose: test build_xfce.py script

source: https://gitlab.com/kevinbowen/xfce-repocapp
version: 0.8.7
updated: 20230315
@author: kevin.bowen@gmail.com
"""

import unittest

from build_xfce import build_xfce  # noqa: F401
from cappdata import component_list  # noqa: F401

arg = "bindings"


class TestBuildXfce(unittest.TestCase):
    """Test the build_xfce() function of build_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print("setUp")
        pass

    def tearDown(self):
        """Tear down the test features."""
        print("tearDown\n")
        pass

    def test_build_xfce(self):
        """testing build_xfce() function."""
        pass


class TestMain(unittest.TestCase):
    """Test the main() function of build_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print("setUp")
        pass

    def tearDown(self):
        """Tear down the test features."""
        print("tearDown\n")
        pass

    def test_main(self):
        """testing main() function in build_xfce.py"""
        pass


if __name__ == "__main__":
    unittest.main()
