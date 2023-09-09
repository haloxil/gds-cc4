"""
This module extracts selected fields and store the data as restaurants.csv.
"""
import json
import urllib.request
import pandas as pd
import numpy as np

URL = (
    "https://raw.githubusercontent.com/"
    "Papagoat/brain-assessment/main/restaurant_data.json"
)
with urllib.request.urlopen(URL) as response:
    data = json.load(response)

country_codes_df = pd.read_excel('Country-Code.xlsx')

with open('restaurant.json', 'r', encoding='utf-8') as f:
    metadata = json.load(f)

df = pd.json_normalize(data, 'restaurants')
selected_cols = [metadata['restaurant_id'], metadata['restaurant_name'],
                 metadata['country'], metadata['city'],
                 metadata['user_rating_votes'],
                 metadata['user_aggregate_rating'], metadata['cuisines']]
df = df[selected_cols]

df = pd.merge(df, country_codes_df, left_on=metadata['country'],
              right_on='Country Code', how='left')
df = df.drop(columns={
    metadata['country'],
    'Country Code'
})
df = df.replace(r'^\s*$', np.nan, regex=True)
df = df.fillna('NA')

df = df.rename(columns={
    metadata['restaurant_id']: 'Restaurant Id',
    metadata['restaurant_name']: 'Restaurant Name',
    metadata['city']: 'City',
    metadata['user_rating_votes']: 'User Rating Votes',
    metadata['user_aggregate_rating']: 'User Aggregate Rating',
    metadata['cuisines']: 'Cuisines'
})

column_order = [
    'Restaurant Id',
    'Restaurant Name',
    'City',
    'Country',
    'User Rating Votes',
    'User Aggregate Rating',
    'Cuisines'
]

df = df.reindex(columns=column_order)

df.to_csv('restaurants.csv', index=False, encoding='utf-8-sig')
