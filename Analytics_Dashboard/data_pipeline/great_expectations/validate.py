python
import great_expectations as ge
from great_expectations.dataset import PandasDataset

# Define data source location
data_source = "s3://my-data-lake/path/to/data.csv"

# Load the data into a Pandas dataset
dataset = PandasDataset(data_source, expectation_suite_name="my_data_suite")

# Define some simple expectations
dataset.expect_column_values_to_not_be_null("column1")
dataset.expect_column_values_to_not_be_null("column2")
dataset.expect_column_values_to_not_be_null("column3")

# Validate the data against the defined expectations
validation_result = dataset.validate()

# Output the validation results
print(validation_result)
