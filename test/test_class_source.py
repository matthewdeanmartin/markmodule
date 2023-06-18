from markmodule.class_source import serialize_source


class Foobar:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def test_serialize_source():
    foobar = Foobar(123, 456)
    result = serialize_source(type(foobar))
    print(result)
    assert result
