# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "environment": {}
# META   }
# META }

# MARKDOWN ********************

# #### Unit Testing for Dataframe Helper Functions
# ---

# CELL ********************

from runtime.nutterfixture import NutterFixture, tag

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

class DataFrameTestFixture(NutterFixture):
  def before_all(self):
      # Existing DataFrameTestFixture setup
      self.expected_schema = StructType([
          StructField('col_a', IntegerType(), True),
          StructField('col_b', StringType(), True),
          StructField('col_c', StringType(), True),
          StructField('col_d', StringType(), True)
      ])

      self.sample_df = spark.createDataFrame(
          [
              (1, '100.0', '500', '2024-01-01'), 
              (1, '100.0', '500', '2024-01-02')
          ], self.expected_schema)
      
      # DateRangeTest setup
      self.start_date = date(2024, 1, 1)
      self.end_date = date(2024, 1, 5)
      self.expected_output = [
          {"DateKey": 20240101, "Date": date(2024, 1, 1), "Day": 1, "Month": 1, "Year": 2024, "DayOfWeek": "Monday", "Quarter": 1, "Half": 1},
          {"DateKey": 20240102, "Date": date(2024, 1, 2), "Day": 2, "Month": 1, "Year": 2024, "DayOfWeek": "Tuesday", "Quarter": 1, "Half": 1},
          {"DateKey": 20240103, "Date": date(2024, 1, 3), "Day": 3, "Month": 1, "Year": 2024, "DayOfWeek": "Wednesday", "Quarter": 1, "Half": 1},
          {"DateKey": 20240104, "Date": date(2024, 1, 4), "Day": 4, "Month": 1, "Year": 2024, "DayOfWeek": "Thursday", "Quarter": 1, "Half": 1},
          {"DateKey": 20240105, "Date": date(2024, 1, 5), "Day": 5, "Month": 1, "Year": 2024, "DayOfWeek": "Friday", "Quarter": 1, "Half": 1}
      ]
  
  def assertion_add_hash_key(self):
      df_with_hash = add_hash_key(self.sample_df, 'hash_key', ['col_a', 'col_b'])
      assert 'hash_key' in df_with_hash.columns
  
  def assertion_deduplicate_by_keys(self):
      deduped_df = deduplicate_by_keys(self.sample_df, ['col_a'], ['col_d'])
      assert deduped_df.count() == 1

  def assertion_generate_date_range(self):
      result = generate_date_range(self.start_date, self.end_date)
      
      # Check if the result has the correct number of dates
      assert len(result) == 5, f"Expected 5 dates, but got {len(result)}"
      
      # Check if the result matches the expected output
      assert result == self.expected_output, "Generated date range does not match expected output"

  def assertion_generate_date_range_single_day(self):
      single_day = date(2024, 1, 1)
      result = generate_date_range(single_day, single_day)
      
      # Check if the result has only one date
      assert len(result) == 1, f"Expected 1 date, but got {len(result)}"
      
      # Check if the single date is correct
      expected_single_day_result = {
          "DateKey": 20240101,
          "Date": single_day,
          "Day": 1,
          "Month": 1,
          "Year": 2024,
          "DayOfWeek": "Monday",
          "Quarter": 1,
          "Half": 1
      }
      assert result[0] == expected_single_day_result, f"Single day result is incorrect. Expected {expected_single_day_result}, but got {result[0]}"

  def assertion_generate_date_range_invalid_input(self):
      # Test with end_date before start_date
      invalid_start = date(2024, 1, 5)
      invalid_end = date(2024, 1, 1)
      result = generate_date_range(invalid_start, invalid_end)
      
      # Check if the result is an empty list
      assert result == [], "Expected an empty list for invalid date range"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
