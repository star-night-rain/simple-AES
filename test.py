import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        temp = list()
        temp.append('12')
        temp.append('34')
        a = enumerate(temp)
        print(a)
        # self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
