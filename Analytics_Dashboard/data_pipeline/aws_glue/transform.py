python
import pandas as pd

# read in data from AWS Glue extract step
df = pd.read_csv("s3://my-bucket/my-data.csv")

# transform the data
df = df.drop_duplicates()
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month

# write transformed data to S3 for use by downstream systems
df.to_csv("s3://my-bucket/my-transformed-data.csv", index=False)
