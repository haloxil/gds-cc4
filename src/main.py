"""
main.py
"""
import json
import urllib.request
import pandas as pd
# import boto3

def main():
    """
    Configures df and metadata
    """
    url = (
        "https://raw.githubusercontent.com/"
        "Papagoat/brain-assessment/main/restaurant_data.json"
    )
    with urllib.request.urlopen(url) as response:
        data = json.load(response)

    with open('restaurant_metadata.json', 'r', encoding='utf-8') as file:
        metadata = json.load(file)

    # This method uses s3 to retrieve the files
    '''
    s3_client = boto3.client('s3')
    bucket = 'govtech-cc4'

    data_response = s3_client.get_object(Bucket=bucket, Key='files/restaurant.json')
    data = json.loads(data_response['Body'].read().decode('utf-8'))
    metadata_response = s3_client.get_object(Bucket=bucket, Key='files/restaurant_metadata.json')
    metadata = json.loads(metadata_response['Body'].read().decode('utf-8'))
    '''

    main_df = pd.json_normalize(data, ['restaurants'])

    return main_df, metadata
