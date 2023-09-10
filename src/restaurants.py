"""
This module extracts selected fields and store the data as restaurants.csv.
"""
import pandas as pd
import main
from utils import populate_empty_values

df_restaurants, metadata = main.main()
country_codes_df = pd.read_excel('Country-Code.xlsx')

restaurant_id = metadata['restaurant_id']
restaurant_name = metadata['restaurant_name']
country = metadata['country']
city = metadata['city']
user_rating_votes = metadata['user_rating_votes']
user_aggregate_rating = metadata['user_aggregate_rating']
cuisines = metadata['cuisines']

selected_cols = [restaurant_id, restaurant_name, country, city,
                 user_rating_votes, user_aggregate_rating, cuisines]
df_restaurants = df_restaurants[selected_cols]

df_restaurants = pd.merge(df_restaurants, country_codes_df, left_on=country,
                          right_on='Country Code', how='left')

df_restaurants = df_restaurants.drop(columns={
    country,
    'Country Code'
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
