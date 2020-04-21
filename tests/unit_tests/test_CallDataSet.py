import unittest
import cellyzer.core as core
import cellyzer.io as io


class TestCallDataSet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # before all the tests
        cls.user1 = "7163185791"
        cls.user2 = "7187432175"
        cls.user3 = '7641036117'
        cls.callDataSet = core.CallDataSet()
        call_file_path = "../../dataset/my_test_data/calls.csv"
        cls.callDataSet = io.read_call(call_file_path)

    @classmethod
    def tearDownClass(cls):
        # after all the tests
        pass

    def setUp(self):
        # run before each test
        pass

    def tearDown(self):
        # run after each test
        pass

    # functions

    def test_get_records(self):
        print("test - get records")

    def test_get_all_users(self):
        print("test - get all users")

    def test_get_connected_users(self):
        print("test - get connected users")

    def test_connection_matrix(self):
        print("test - connection matrix")

    def test_get_connections(self):
        print("test - get connections")

    def test_get_most_active_time(self):
        print("test - most active time")

        user1_result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 1, 12: 1, 13: 1, 14: 0,
                        15: 5, 16: 0, 17: 0, 18: 4, 19: 0, 20: 0, 21: 1, 22: 0, 23: 0}
        self.assertEqual(self.callDataSet.get_most_active_time(user=self.user1), user1_result)

        user2_result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0,
                        15: 4, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0}
        self.assertEqual(self.callDataSet.get_most_active_time(user=self.user2), user2_result)

        user3_result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 3, 8: 4, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0,
                        15: 0, 16: 0, 17: 0, 18: 0, 19: 1, 20: 0, 21: 0, 22: 0, 23: 0}
        self.assertEqual(self.callDataSet.get_most_active_time(user=self.user3), user3_result)

        with self.assertRaises(TypeError):
            self.callDataSet.get_most_active_time(12.34)
            self.callDataSet.get_most_active_time([self.user1])
            self.callDataSet.get_most_active_time({})

    def test_get_close_contacts(self):
        print('test - close contacts')

        user1_result = {'7187432175': 4, '7230262224': 1}
        self.assertEqual(self.callDataSet.get_close_contacts(user=self.user1, top_contact=2), user1_result)

        user2_result = {'7163185791': 4}
        self.assertEqual(self.callDataSet.get_close_contacts(user=self.user2), user2_result)

        user3_result = {'1666472054': 1, '7371326239': 1, '7681546436': 1, '7981267897': 1}
        self.assertEqual(self.callDataSet.get_close_contacts(user=self.user3, top_contact=4), user3_result)

        with self.assertRaises(TypeError):
            self.callDataSet.get_close_contacts(12.3)
            self.callDataSet.get_close_contacts([self.user1])
            self.callDataSet.get_close_contacts({})

    def test_get_call_records_by_antenna_id(self):
        print('test - get call records by antenna id')

        cell1_result = 8
        self.assertEqual(len(self.callDataSet.get_call_records_by_antenna_id(cell_id=1)), cell1_result)

        cell2_result = 25
        self.assertEqual(len(self.callDataSet.get_call_records_by_antenna_id(cell_id=2)), cell2_result)

        self.assertEqual(len(self.callDataSet.get_call_records_by_antenna_id(cell_id=20)), 0)

    def test_get_ignored_call_details(self):
        print("test - get ignored call details")

        self.assertEqual(self.callDataSet.get_ignored_call_details(user=self.user1), [])
        self.assertEqual(self.callDataSet.get_ignored_call_details(user=self.user2), [])

        user3_result = [{'other user': '7681546436', 'date': '11-02-1980', 'time stamp': '08:06:18', 'cell ID': '5'}]
        self.assertEqual(self.callDataSet.get_ignored_call_details(user=self.user3), user3_result)

        with self.assertRaises(TypeError):
            self.callDataSet.get_ignored_call_details(12.3)
            self.callDataSet.get_ignored_call_details([self.user1])
            self.callDataSet.get_ignored_call_details({})


if __name__ == '__main__':
    unittest.main()