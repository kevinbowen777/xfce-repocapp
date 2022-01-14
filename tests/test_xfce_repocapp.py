import unittest

from xfce_repocapp import __version__
from xfce_repocapp import __author__


def test_author():
    assert __author__ == 'Kevin Bowen <kevin.bowen@gmail.com>'


def test_version():
    assert __version__ == '0.8.6'


class TestMainMenu(unittest.TestCase):
    """Test the clone_xfce() function of clone_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print('setUp')
        pass
        # begins with self.

    def tearDown(self):
        """Tear down the test features."""
        print('tearDown\n')
        pass

    def test_xfce_repocapp(self):
        """testing clone_xfce() function"""
        self.assertIsNotNone(clone_xfce(component=bindings,
                                        comp_list=bindings))


class TestSubMenus(unittest.TestCase):
    """Test the main() function of clone_xfce.py."""

    def setUp(self):
        """Set up the test features."""
        print('setUp')
        pass

    def tearDown(self):
        """Tear down the test features."""
        print('tearDown\n')
        pass

    def test_main(self):
        """testing main() function in clone_xfce.py"""
        self.assertIsNotNone(main(bindings))


if __name__ == '__main__':
    unittest.main()
