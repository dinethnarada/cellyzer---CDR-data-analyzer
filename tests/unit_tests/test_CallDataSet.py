import unittest
import cellyzer.core as core
import cellyzer.io as io


class TestCallDataSet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # before all the tests
        cls.user1 = "7163185791"
        cls.user2 = "7187432175"
        cls.call_obj = core.CallDataSet()
        print("setup class")

    @classmethod
    def tearDownClass(cls):
        # after all the tests
        print("teardown class")

    def setUp(self):
        # run before each test
        print("setUp")

    def tearDown(self):
        # run after each test
        print("Teardown")

    def test_get_most_active_time(self):
        result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0}
        self.assertEqual(self.call_obj.get_most_active_time(user=self.user1), result)
        print("test - most active time")


if __name__ == '__main__':
    unittest.main()
