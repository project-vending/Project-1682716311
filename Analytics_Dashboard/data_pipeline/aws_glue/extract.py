python
import boto3
import pandas as pd
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, ['bucket_name'])

# Initialize the S3 client
s3 = boto3.client('s3')

# Extract data from S3 bucket
bucket_name = args['bucket_name']
object_key = 'example/csv/file.csv'

response = s3.get_object(Bucket=bucket_name, Key=object_key)

# Load CSV file contents into a Pandas DataFrame
df = pd.read_csv(response['Body'])

# Optional: perform additional data transformations
# df = add_column(df, 'new_column', 0)

# Save the data as a CSV file in the same bucket
df.to_csv(f's3://{bucket_name}/example/processed/file.csv', index=False)

