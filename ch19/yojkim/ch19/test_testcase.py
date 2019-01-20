from testcase import TestCase
from wasrun import WasRun


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)

    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetUp)


TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
