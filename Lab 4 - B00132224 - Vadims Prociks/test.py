import HtmlTestRunner
import unittest
class TestStringMethods(unittest.TestCase):
    def test_twoValuesAreEqual(self):
        value1=True
        value2=True
        self.assertEqual(value1, value2)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_output'))