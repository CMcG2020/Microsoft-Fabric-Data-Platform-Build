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

# #### Unit Testing for Metadata Helper Functions
# ---

# CELL ********************

from runtime.nutterfixture import NutterFixture, tag

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

class MetadataTestFixture(NutterFixture):
    def before_all(self):
        self.dict_schema = [
            {'name': 'id', 'source': None, 'dataType': IntegerType()}, 
            {'name': 'field_1', 'source': 'name', 'dataType': StringType()}, 
            {'name': 'field_2', 'source': 'busines_criticality', 'dataType': StringType()}
            ]   

        sample_schema = ['id', 'field_1', 'field_2', 'field_3']
        self.sample_df = spark.createDataFrame([(1, '100.0', '500', 'true')], sample_schema)

    def assertion_add_pipeline_metadata(self):
        output_df = add_pipeline_metadata(self.sample_df, '2024-01-01', '2024-01-01', 'SourceSystem', 'application')
        for f in ['TableName', 'ReceiptDate', 'AllocatedDate', 'PipelineUpdatedDate', 'SourceSystem']:
            assert f in output_df.columns, f'{f} field not resulting df columns: {output_df.columns}'

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
