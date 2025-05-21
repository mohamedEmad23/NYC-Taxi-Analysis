import unittest
from src.data.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = DataProcessor()

    def test_clean_data(self):
        # Test cleaning data with missing values
        raw_data = {
            'fare_amount': [10, None, 5, 20],
            'extra': [0.5, 0.5, None, 1.0],
            'mta_tax': [0.5, 0.5, 0.5, None],
            'tip_amount': [1.5, 0, 0.5, 2.0],
            'tolls_amount': [0, 0, 0, 0],
            'passenger_count': [1, 2, 1, None]
        }
        cleaned_data = self.processor.clean_data(raw_data)
        self.assertEqual(len(cleaned_data), 3)  # Expecting 3 rows after cleaning

    def test_calculate_trip_duration(self):
        # Test trip duration calculation
        raw_data = {
            'pickup_datetime': ['2023-01-01 10:00:00', '2023-01-01 10:30:00'],
            'dropoff_datetime': ['2023-01-01 10:15:00', '2023-01-01 10:45:00']
        }
        durations = self.processor.calculate_trip_duration(raw_data)
        self.assertEqual(durations[0], 15)  # Expecting 15 minutes
        self.assertEqual(durations[1], 15)  # Expecting 15 minutes

    def test_calculate_total_cost(self):
        # Test total cost calculation
        raw_data = {
            'fare_amount': [10, 20],
            'extra': [0.5, 1.0],
            'mta_tax': [0.5, 0.5],
            'tip_amount': [1.5, 2.0],
            'tolls_amount': [0, 0]
        }
        total_costs = self.processor.calculate_total_cost(raw_data)
        self.assertEqual(total_costs[0], 12.5)  # Expecting 12.5
        self.assertEqual(total_costs[1], 24.0)  # Expecting 24.0

if __name__ == '__main__':
    unittest.main()