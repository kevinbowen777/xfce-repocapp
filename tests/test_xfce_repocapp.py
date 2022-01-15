from xfce_repocapp import __author__
from xfce_repocapp import __version__
from xfce_repocapp import __doc__
from xfce_repocapp import __releasedate__


def test_author():
    assert __author__ == 'Kevin Bowen <kevin.bowen@gmail.com>'


def test_version():
    assert __version__ == '0.8.6'


def test_doc():
    assert __doc__ == 'A collection of scripts to maintain ' \
                      'local Xfce repositories'


def test_releasedate():
    assert __releasedate__ == '20220101'
