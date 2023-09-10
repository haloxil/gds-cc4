"""
This module extracts selected fields and store the data as threshold.csv.
"""
import pandas as pd
import main

df_threshold, metadata = main.main()

user_text_rating = metadata['user_text_rating']
user_aggregate_rating = metadata['user_aggregate_rating']
text_rating_rules = metadata['rules']['text_rating']

selected_cols = [user_text_rating, user_aggregate_rating]
df_threshold = df_threshold[selected_cols]
df_threshold[user_aggregate_rating] = pd.to_numeric(
    df_threshold[user_aggregate_rating], errors='coerce')

min_ratings = df_threshold.groupby(
    user_text_rating)[user_aggregate_rating].min().sort_values()
min_ratings_df = min_ratings.reset_index()
min_ratings_df = min_ratings_df[min_ratings_df
                                [user_text_rating].isin(text_rating_rules)]

min_ratings_df = min_ratings_df.rename(columns={
    user_text_rating: 'User Text Rating',
    user_aggregate_rating: 'User Aggregate Rating'
})

min_ratings_df.to_csv('threshold.csv', index=False, encoding='utf-8-sig')
