from sphinxcontrib.runcmd.utils import Singleton


class TheSingleton(object, metaclass=Singleton):  # noqa: E999
    pass


def test_singleton():
    a = TheSingleton()
    b = TheSingleton()

    assert a == b
    assert hash(a) == hash(b)
