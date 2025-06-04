# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "environment": {
# META       "environmentId": "894291a9-f8d5-4ea0-8d4d-a41d3d9b7541",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Parent Helper Functions
# ---
# This notebook stores all of the `%run` magic commands to call every available helper functions. This avoids having to include multiple magic command cell blocks in individual transformation notebooks.

# CELL ********************

from pyspark.sql.types import StructType, StructField, StringType, BooleanType, DateType, DoubleType, FloatType, IntegerType, LongType, ShortType, DecimalType, TimestampType, ArrayType
from pyspark.sql import SparkSession, DataFrame, Row 
from pyspark.sql.utils import AnalysisException
from pyspark.sql.window import Window
from pyspark.sql.functions import explode, lit, col, when, row_number
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, date, timezone
from delta.tables import DeltaTable
from typing import List, Dict, Optional, Union, Any 
from notebookutils import mssparkutils
from requests.auth import HTTPBasicAuth
from trident_token_library_wrapper import PyTridentTokenLibrary as tl
from itertools import chain
from pprint import pprint
from azure.storage.filedatalake import DataLakeServiceClient
from concurrent.futures import ThreadPoolExecutor
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
# Data Quality
from soda.scan import Scan
from soda.sampler.sampler import Sampler
from soda.sampler.sample_context import SampleContext
from rich import inspect
from functools import reduce
from pathlib import Path
import uuid
import os
import pyspark.sql.functions as F
import sempy.fabric as fabric
from typing import Union
import pandas as pd
import textwrap
import requests
import logging
import base64
import json
import time
import sys
import re
import concurrent.futures

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Set up logging configuration to be used across pipelines
logging.basicConfig(
    level=logging.INFO,  # This ensures INFO level and above will be logged
    format='%(asctime)s - %(levelname)s - %(message)s',  # Adds timestamp and level info to each log
    handlers=[logging.StreamHandler()],  # Logs will be printed to the console
    force=True  # This will override any previous logging configuration in Jupyter
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_configs_global

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_configs_ingestion

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_configs_conformed

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_configs_pipelines

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_helper_functions_dataframe

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_helper_functions_metadata

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_helper_functions_readers

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_helper_functions_writers

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_helper_functions_pipeline

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_helper_functions_tests

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
