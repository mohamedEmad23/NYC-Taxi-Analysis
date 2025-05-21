# NYC Taxi Analysis Project

## Overview
The NYC Taxi Analysis project aims to optimize urban mobility solutions by analyzing yellow taxi trip data in New York City. The project involves data cleaning, exploration, and modeling to generate insights that support decision-making for drivers and riders. The analysis leverages Apache Cassandra for data storage and Apache Spark for data processing and machine learning.

## Project Structure
```
nyc-taxi-analysis
├── src
│   ├── config
│   │   └── config.py          # Configuration settings for Cassandra and Spark
│   ├── data
│   │   ├── data_loader.py      # Loads datasets and handles initial validation
│   │   └── data_processor.py    # Cleans and processes the data
│   ├── db
│   │   └── cassandra_client.py  # Manages Cassandra database connections
│   ├── models
│   │   ├── classifier.py        # Implements machine learning models
│   │   └── feature_engineering.py # Contains feature engineering functions
│   ├── queries
│   │   └── spark_queries.py      # Spark SQL queries for data insights
│   ├── utils
│   │   ├── cassandra_utils.py    # Utility functions for Cassandra interactions
│   │   └── spark_utils.py        # Utility functions for Spark operations
│   └── main.py                   # Entry point for the application
├── notebooks
│   ├── exploratory_data_analysis.ipynb # Jupyter notebook for exploratory analysis
│   ├── data_cleaning.ipynb       # Jupyter notebook documenting data cleaning
│   └── model_evaluation.ipynb     # Jupyter notebook for model evaluation
├── tests
│   ├── test_data_processor.py      # Unit tests for data processing functions
│   ├── test_cassandra_client.py     # Unit tests for Cassandra client functions
│   └── test_models.py               # Unit tests for machine learning models
├── requirements.txt                 # Python dependencies for the project
├── setup.py                         # Packaging information for the project
├── .gitignore                       # Files and directories to ignore in version control
└── README.md                        # Project documentation
```

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd nyc-taxi-analysis
   ```

2. **Install Dependencies**
   Ensure you have Python 3.x installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Configure Astra DB**
   - Create an account on [DataStax Astra](https://astra.datastax.com) if you don't have one
   - Create a database and get the API endpoint
   - Generate a token with appropriate permissions
   - Create a `.env` file in the project root with your Astra DB credentials:
   ```
   ASTRA_DB_TOKEN=your_token_here
   ASTRA_DB_API_ENDPOINT=your_api_endpoint_here
   ```

4. **Test Astra DB Connection**
   Run the test script to verify your connection:
   ```bash
   python -m src.utils.test_astra_connection
   ```

5. **Local Cassandra Setup (Optional)**
   If you want to also use a local Cassandra setup:
   - Install Apache Cassandra locally
   - Update the connection settings in your `.env` file:
   ```
   CASSANDRA_HOST=localhost
   CASSANDRA_PORT=9042
   CASSANDRA_KEYSPACE=nyc_taxi
   ```

4. **Run the Application**
   Execute the main application:
   ```bash
   python src/main.py
   ```

## Usage Guidelines
- Use the Jupyter notebooks in the `notebooks` directory for exploratory data analysis and model evaluation.
  - Start with `notebooks/astra_db_exploration.ipynb` to explore Astra DB functionality.
  - Use `notebooks/exploratory_data_analysis.ipynb` for initial data exploration.
  - Use `notebooks/data_cleaning.ipynb` for data preprocessing steps.
  - Use `notebooks/model_evaluation.ipynb` for evaluating machine learning models.
- The `src` directory contains the core functionality, including data loading, processing, querying, and modeling.
- Unit tests are located in the `tests` directory to ensure the integrity of the codebase.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.