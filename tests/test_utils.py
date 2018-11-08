from sphinxcontrib.runcmd.utils import Singleton


class TheSingleton(Singleton):
    pass


def test_singleton():
    a = TheSingleton()
    b = TheSingleton()

    assert a == b
    assert hash(a) == hash(b)
