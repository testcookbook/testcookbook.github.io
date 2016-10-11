class AdderLibrary(object):
    """
    Tests for AdderLibrary
    """

    def __init__(self):
        self._result=0

    def add_input(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def total(self, expected):
        self._result = self.a + self.b
        if self._result != int(expected):
            raise AssertionError('%s != %s' % (self._result, expected))
