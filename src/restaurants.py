"""
This module extracts selected fields and store the data as restaurants.csv.
"""
import pandas as pd
import numpy as np
import main

df_restaurants, metadata = main.main()

country_codes_df = pd.read_excel('Country-Code.xlsx')

selected_cols = [metadata['restaurant_id'], metadata['restaurant_name'],
                 metadata['country'], metadata['city'],
                 metadata['user_rating_votes'],
                 metadata['user_aggregate_rating'], metadata['cuisines']]
df_restaurants = df_restaurants[selected_cols]

df_restaurants = pd.merge(df_restaurants, country_codes_df, left_on=metadata['country'],
              right_on='Country Code', how='left')
df_restaurants = df_restaurants.drop(columns={
    metadata['country'],
    'Country Code'
})
df_restaurants = df_restaurants.replace(r'^\s*$', np.nan, regex=True)
df_restaurants = df_restaurants.fillna('NA')

df_restaurants = df_restaurants.rename(columns={
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

df_restaurants = df_restaurants.reindex(columns=column_order)

df_restaurants.to_csv('restaurants.csv', index=False, encoding='utf-8-sig')