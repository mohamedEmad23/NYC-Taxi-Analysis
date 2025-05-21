import unittest
from src.db.cassandra_client import CassandraClient

class TestCassandraClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = CassandraClient()
        cls.client.connect()

    @classmethod
    def tearDownClass(cls):
        cls.client.close()

    def test_insert_data(self):
        # Sample data for testing
        sample_data = {
            'trip_id': '1',
            'pickup_location': 'Location A',
            'dropoff_location': 'Location B',
            'fare_amount': 10.0,
            'tip_amount': 2.0,
            'total_cost': 12.0
        }
        result = self.client.insert_trip_data(sample_data)
        self.assertTrue(result)

    def test_query_data(self):
        # Assuming a trip with trip_id '1' exists
        trip_id = '1'
        result = self.client.query_trip_data(trip_id)
        self.assertIsNotNone(result)
        self.assertEqual(result['trip_id'], trip_id)

    def test_query_non_existent_data(self):
        trip_id = '999'  # Assuming this trip_id does not exist
        result = self.client.query_trip_data(trip_id)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()