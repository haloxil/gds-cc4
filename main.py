"""
This module extracts selected fields and store the data as restaurants.csv.
"""
import json
import urllib.request
import pandas as pd

URL = (
    "https://raw.githubusercontent.com/"
    "Papagoat/brain-assessment/main/restaurant_data.json"
)
with urllib.request.urlopen(URL) as response:
    data = json.load(response)

with open('restaurant.json', 'r', encoding='utf-8') as f:
    metadata = json.load(f)

df = pd.json_normalize(data, 'restaurants')
selected_cols = [metadata['restaurant_id'], metadata['restaurant_name'],
                 metadata['country'], metadata['city'],
                 metadata['user_rating_votes'],
                 metadata['user_aggregate_rating'], metadata['cuisines']]
df = df[selected_cols]

df = df.rename(columns={
    metadata['restaurant_id']: 'Restaurant Id',
    metadata['restaurant_name']: 'Restaurant Name',
    metadata['country']: 'Country',
    metadata['city']: 'City',
    metadata['user_rating_votes']: 'User Rating Votes',
    metadata['user_aggregate_rating']: 'User Aggregate Rating',
    metadata['cuisines']: 'Cuisines'
})

print(df.columns)
