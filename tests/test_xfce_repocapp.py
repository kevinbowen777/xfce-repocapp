from xfce_repocapp import __version__
from xfce_repocapp import __author__


def test_author():
    assert __author__ == 'Kevin Bowen <kevin.bowen@gmail.com>'


def test_version():
    assert __version__ == '0.8.5'
