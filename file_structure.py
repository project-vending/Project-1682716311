
import os

# create project directory
os.mkdir("Analytics_Dashboard")

# create subdirectories for data pipeline
os.mkdir("Analytics_Dashboard/data_pipeline")
os.mkdir("Analytics_Dashboard/data_pipeline/aws_glue")
os.mkdir("Analytics_Dashboard/data_pipeline/great_expectations")
os.mkdir("Analytics_Dashboard/data_pipeline/streamlit")

# create empty files for data pipeline
open("Analytics_Dashboard/data_pipeline/aws_glue/extract.py", "w").close()
open("Analytics_Dashboard/data_pipeline/aws_glue/transform.py", "w").close()

# create empty files for great expectations
open("Analytics_Dashboard/data_pipeline/great_expectations/validate.py", "w").close()

# create empty files for streamlit
open("Analytics_Dashboard/data_pipeline/streamlit/dashboard.py", "w").close()
