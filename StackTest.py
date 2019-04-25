import unittest
class StackTest(unittest.Testcase):
    def setUp(self):
        self.s = Stack()

    def testNewStack(self):
        self.asserTrue(self.s.isEmpty())
        self.assertEqual(self.s.size(),0)

    def tesPushes(self):
        nPushes = 6
        for i in range(nPushes):
            self.s.push("item")
        self.assertFalse(self.s.isEmpty())
        self.assertEquals(self.s.size(),nPushes)