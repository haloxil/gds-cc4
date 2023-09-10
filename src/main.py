"""
main.py
"""
import json
import urllib.request
import pandas as pd

def main():
    URL = (
        "https://raw.githubusercontent.com/"
        "Papagoat/brain-assessment/main/restaurant_data.json"
    )
    with urllib.request.urlopen(URL) as response:
        data = json.load(response)

    with open('restaurant.json', 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    df = pd.json_normalize(data, ['restaurants'])

    return df, metadata