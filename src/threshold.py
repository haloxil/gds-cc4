"""
This module extracts selected fields and store the data as restaurant_events.csv.
"""
import pandas as pd
import main 


df_threshold, metadata = main.main()

selected_cols = [metadata['user_text_rating'], metadata['user_aggregate_rating']]
df_threshold  = df_threshold [selected_cols]

df_threshold[metadata['user_aggregate_rating']] = pd.to_numeric(df_threshold[metadata['user_aggregate_rating']], errors='coerce')
min_ratings = df_threshold.groupby(metadata['user_text_rating'])[metadata['user_aggregate_rating']].min().sort_values()

min_ratings_df = min_ratings.reset_index()
min_ratings_df= min_ratings_df[min_ratings_df[metadata['user_text_rating']].isin(metadata['rules']['text_rating'])]

min_ratings_df = min_ratings_df.rename(columns={
    metadata['user_text_rating']: 'User Text Rating',
    metadata['user_aggregate_rating']: 'User Aggregate Rating'
})

min_ratings_df.to_csv('threshold.csv', index=False, encoding='utf-8-sig')