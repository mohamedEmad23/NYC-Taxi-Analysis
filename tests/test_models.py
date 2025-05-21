import unittest
from pyspark.sql import SparkSession
from src.models.classifier import Classifier
from src.models.feature_engineering import FeatureEngineering

class TestModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder \
            .appName("NYC Taxi Analysis Test") \
            .getOrCreate()
        cls.classifier = Classifier()
        cls.feature_engineering = FeatureEngineering()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_high_tip_feature(self):
        data = [(1, 10.0, 1.5), (2, 20.0, 3.0), (3, 15.0, 2.0)]
        df = self.spark.createDataFrame(data, ["passenger_count", "fare_amount", "tip_amount"])
        df = self.feature_engineering.create_high_tip_column(df)
        result = df.select("high_tip").collect()
        expected = [(0,), (1,), (0,)]
        self.assertEqual(result, expected)

    def test_classifier_training(self):
        data = [(1, 10.0, 1.5, 5.0), (2, 20.0, 3.0, 10.0)]
        df = self.spark.createDataFrame(data, ["passenger_count", "fare_amount", "tip_amount", "trip_distance"])
        df = self.feature_engineering.create_high_tip_column(df)
        model = self.classifier.train_model(df)
        self.assertIsNotNone(model)

    def test_classifier_prediction(self):
        data = [(1, 10.0, 1.5, 5.0)]
        df = self.spark.createDataFrame(data, ["passenger_count", "fare_amount", "tip_amount", "trip_distance"])
        df = self.feature_engineering.create_high_tip_column(df)
        model = self.classifier.train_model(df)
        predictions = self.classifier.predict(df, model)
        self.assertEqual(len(predictions), 1)

if __name__ == '__main__':
    unittest.main()