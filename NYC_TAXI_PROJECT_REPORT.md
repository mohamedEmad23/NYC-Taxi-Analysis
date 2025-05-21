# NYC Taxi Data Project Report

## Overview
This document provides a comprehensive summary of the NYC Taxi Analysis project, including the data processing steps, features created, and visualizations produced.

## Original Columns Status

The following columns from the original `taxi_trip_data.csv` were handled as follows:

1. **store_and_fwd_flag**: This column was dropped during the final column selection as it was deemed not critical for the analysis.

2. **extra**, **mta_tax**, **tolls_amount**, **imp_surcharge**: These were all used in calculating the `total_cost` feature, but only `tolls_amount` was kept as an individual column in the final dataset.

## Required New Columns Created

The following columns were created for a more enriched analysis and implementation:

1. **trip_duration_mins**: Calculated from the difference between pickup_datetime and dropoff_datetime, converted to minutes.

2. **total_cost**: Calculated using the formula: `fare_amount + extra + mta_tax + tip_amount + tolls_amount + imp_surcharge`

## Additional Enrichment Columns

Beyond the requirements, the following additional features were created to provide deeper insights:

### Time-Based Features
- **pickup_hour**: Hour of day when the trip started
- **pickup_day**: Day of week (1-7) for the pickup
- **pickup_month**: Month of the year for the pickup
- **pickup_year**: Year of the pickup
- **pickup_dayofmonth**: Day of the month for the pickup
- **pickup_weekofyear**: Week number within the year
- **day_type**: Categorized as "weekend" or "weekday"
- **time_of_day**: Categorized as "morning_rush" (6-10am), "midday" (10am-4pm), "evening_rush" (4-8pm), or "night" (8pm-6am)

### Trip Metrics
- **avg_speed_mph**: Trip distance divided by duration in hours
- **cost_per_mile**: Fare amount divided by trip distance
- **tip_percentage**: Tip amount as a percentage of the fare amount

### Location Enhancements
- **pickup_zone_name**: The name of the pickup zone, joined from the zone data
- **dropoff_zone_name**: The name of the dropoff zone, joined from the zone data
- **pickup_borough**: The borough of the pickup location
- **dropoff_borough**: The borough of the dropoff location
- **is_inter_borough**: Boolean flag indicating whether the trip crossed borough boundaries

## Final Dataset Columns and Descriptions

The final processed dataset contains the following columns:

| Column Name | Description | Source |
|-------------|-------------|--------|
| vendor_id | ID of the vendor providing the trip data | Original |
| pickup_datetime | Date and time when the trip started | Original |
| dropoff_datetime | Date and time when the trip ended | Original |
| passenger_count | Number of passengers in the vehicle | Original |
| pickup_location_id | TLC Taxi Zone ID of the pickup location | Original |
| pickup_zone_name | Name of the pickup zone | Joined from zone data |
| pickup_borough | Borough of the pickup location | Joined from zone data |
| dropoff_location_id | TLC Taxi Zone ID of the dropoff location | Original |
| dropoff_zone_name | Name of the dropoff zone | Joined from zone data |
| dropoff_borough | Borough of the dropoff location | Joined from zone data |
| is_inter_borough | Whether the trip crossed borough boundaries | Derived |
| trip_distance | Trip distance in miles | Original |
| trip_duration_mins | Duration of the trip in minutes | **Required new column** |
| avg_speed_mph | Average speed in miles per hour | Derived |
| fare_amount | Base fare amount in USD | Original |
| tip_amount | Tip amount in USD | Original |
| tip_percentage | Tip as percentage of the fare | Derived |
| total_cost | Total trip cost (fare + extras + taxes + tips) | **Required new column** |
| cost_per_mile | Cost per mile traveled | Derived |
| pickup_hour | Hour of the day (0-23) when pickup occurred | Derived |
| pickup_day | Day of week (1-7) when pickup occurred | Derived |
| pickup_month | Month (1-12) when pickup occurred | Derived |
| pickup_year | Year when pickup occurred | Derived |
| day_type | Classification as "weekend" or "weekday" | Derived |
| time_of_day | Time period classification | Derived |
| payment_type | Method of payment | Original |
| rate_code | Rate code for the trip | Original |

## Data Cleaning Steps Implemented

The project implemented comprehensive data cleaning:

1. **Removed invalid entries**:
   - Negative or zero trip distances
   - Negative fare amounts
   - Invalid passenger counts (0 or >6)
   - Trips where dropoff time was before pickup time
   - Unreasonably long trips (>24 hours)

2. **Handled missing values** using median imputation for numeric columns

3. **Fixed data types** for all columns to ensure consistency

## Data Storage

The cleaned and enriched dataset was stored in:
- Parquet format for efficient Spark processing: `/root/DevDataOps/nyc-taxi-analysis/processed-data/nyc_taxi_processed.parquet`
- CSV format for general access: `/root/DevDataOps/nyc-taxi-analysis/processed-data/nyc_taxi_processed.csv`
- A sample CSV with 1000 records for quick reference

## Visualizations Created

Three key visualizations were created to showcase the cleaned data:

1. **Trip Count by Time of Day and Borough**
   - Displays the number of trips for each borough across different times of the day
   - Helps identify peak demand periods for each borough
   - Saved as: `borough_time_trips.png`

2. **Normalized Average Trip Metrics by Borough**
   - Compares average trip distance, duration, and cost across boroughs
   - Values are normalized for better comparison
   - Helps identify differences in trip characteristics by location
   - Saved as: `borough_metrics.png`

3. **Heatmap of Hourly Trips by Day of Week**
   - Shows trip frequency patterns throughout the week
   - Clearly identifies peak hours and days
   - Helps with demand prediction and resource allocation
   - Saved as: `hourly_heatmap.png`

## Using the Processed Data for Analysis

The processed data is ready for advanced analytics and machine learning:

1. **For Spark SQL Queries**:
   ```python
   from pyspark.sql import SparkSession
   
   # Initialize Spark session
   spark = SparkSession.builder \
       .appName("NYC Taxi Analysis") \
       .getOrCreate()
   
   # Load the processed data
   taxi_data = spark.read.parquet("/root/DevDataOps/nyc-taxi-analysis/processed-data/nyc_taxi_processed.parquet")
   
   # Register as temp table for SQL queries
   taxi_data.createOrReplaceTempView("taxi_trips")
   
   # Run SQL query
   result = spark.sql("""
       SELECT pickup_borough, 
              AVG(trip_distance) as avg_distance, 
              AVG(total_cost) as avg_cost
       FROM taxi_trips
       GROUP BY pickup_borough
       ORDER BY avg_cost DESC
   """)
   result.show()
   ```

2. **For Machine Learning**:
   ```python
   from pyspark.ml.feature import VectorAssembler
   from pyspark.ml.regression import LinearRegression
   
   # Prepare features
   feature_cols = ["trip_distance", "passenger_count", "pickup_hour"]
   assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
   data_with_features = assembler.transform(taxi_data)
   
   # Train-test split
   training_data, test_data = data_with_features.randomSplit([0.8, 0.2], seed=42)
   
   # Train model
   lr = LinearRegression(featuresCol="features", labelCol="total_cost")
   model = lr.fit(training_data)
   
   # Evaluate model
   predictions = model.transform(test_data)
   ```

## Conclusion

The project has successfully transformed raw NYC taxi trip data into a clean, feature-rich dataset that can be used for a wide range of analytical and machine learning tasks. The added features provide valuable context for deeper insights into taxi trip patterns, costs, and efficiency metrics.
