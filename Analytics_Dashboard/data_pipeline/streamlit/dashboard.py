
import streamlit as st
import pandas as pd
import boto3

@st.cache
def load_data():
    # replace bucket_name and file_name with your own S3 bucket and file
    s3 = boto3.resource('s3')
    bucket_name = 'my-bucket'
    file_name = 'my-file.csv'
    obj = s3.Object(bucket_name, file_name)
    body = obj.get()['Body'].read()
    data = pd.read_csv(body)
    return data

def main():
    st.title("Analytics Dashboard")
    st.subheader("Data from S3")

    data = load_data()

    st.write(data)

if __name__ == '__main__':
    main()
