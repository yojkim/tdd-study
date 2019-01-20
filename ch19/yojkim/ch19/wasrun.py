from testcase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = True

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = True
