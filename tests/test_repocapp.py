import unittest

from xfce_repocapp.repocapp import main_menu
from xfce_repocapp.repocapp import sub_menus


class TestMainMenu(unittest.TestCase):
    """Test the main_menu() function of repocapp.py."""

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
        """testing main_menu() function"""
        self.assertIsNotNone(main_menu())


class TestSubMenus(unittest.TestCase):
    """Test the sub_menu() function of repocapp.py."""

    def setUp(self):
        """Set up the test features."""
        print('setUp')
        pass

    def tearDown(self):
        """Tear down the test features."""
        print('tearDown\n')
        pass

    def test_main(self):
        """testing main() function in repocapp.py"""
        self.assertEquals(sub_menus('clone'))


if __name__ == '__main__':
    unittest.main()
