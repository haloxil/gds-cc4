"""
This module extracts selected fields and store the data as restaurants.csv.
"""
import pandas as pd
import main
import awswrangler as wr
from utils import populate_empty_values

df_restaurants, metadata = main.main()
# Uncomment if you want to read from s3 instead
# country_codes_df = wr.s3.read_excel('s3://govtech-cc4/files/Country-Code.xlsx') 
country_codes_df = pd.read_excel('Country-Code.xlsx')

restaurant_id = metadata['restaurant_id']
restaurant_name = metadata['restaurant_name']
country_id = metadata['country_id']
city = metadata['city']
user_rating_votes = metadata['user_rating_votes']
user_aggregate_rating = metadata['user_aggregate_rating']
cuisines = metadata['cuisines']
country_code = 'Country Code'

selected_cols = [restaurant_id, restaurant_name, country_id, city,
                 user_rating_votes, user_aggregate_rating, cuisines]
df_restaurants = df_restaurants[selected_cols]

df_restaurants = pd.merge(df_restaurants, country_codes_df, left_on=country_id,
                          right_on=country_code, how='left')

df_restaurants = df_restaurants.drop(columns={
    country_id,
    country_code
})
df_restaurants = populate_empty_values(df_restaurants)

df_restaurants = df_restaurants.rename(columns={
    restaurant_id: 'Restaurant Id',
    restaurant_name: 'Restaurant Name',
    city: 'City',
    user_rating_votes: 'User Rating Votes',
    user_aggregate_rating: 'User Aggregate Rating',
    cuisines: 'Cuisines'
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
