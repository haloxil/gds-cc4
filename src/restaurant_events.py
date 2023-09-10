"""
This module extracts selected fields and store the data as restaurant_events.csv.
"""
import pandas as pd
from datetime import datetime, date, timedelta
import main 


data, metadata = main.main()

df_restaurants = pd.json_normalize(data, ['restaurants'])
df_events = df_restaurants[[metadata['restaurant_id'], metadata['restaurant_name'], 
                            metadata['photo_url'], 'restaurant.zomato_events']]
df_events = df_events.dropna(subset=['restaurant.zomato_events'])
df_events = df_events.explode('restaurant.zomato_events').reset_index(drop=True)

df_events['Event Id'] = df_events['restaurant.zomato_events'].apply(lambda x: x['event']['event_id'])
df_events['Event Title'] = df_events['restaurant.zomato_events'].apply(lambda x: x['event']['title'])
df_events['Event Start Date'] = df_events['restaurant.zomato_events'].apply(lambda x: x['event']['start_date'])
df_events['Event End Date'] = df_events['restaurant.zomato_events'].apply(lambda x: x['event']['end_date'])

df_events['Event Start Date'] = pd.to_datetime(df_events['Event Start Date'])
df_events['Event End Date'] = pd.to_datetime(df_events['Event End Date'])

df_events = df_events[(df_events['Event Start Date'] 
        <= datetime.combine(date(2019, 5, 1), datetime.min.time()) - timedelta(days=1)) 
        & (df_events['Event End Date'] 
        >= datetime.combine(date(2019, 4, 1), datetime.min.time()))]

df_events = df_events.rename(columns={
    metadata['restaurant_id']: 'Restaurant Id',
    metadata['restaurant_name']: 'Restaurant Name',
    metadata['photo_url']: 'Photo URL',
})

column_order = [
    'Event Id',
    'Restaurant Id',
    'Restaurant Name',
    'Photo URL',
    'Event Title',
    'Event Start Date',
    'Event End Date'
]

df_events = df_events.reindex(columns=column_order)

df_events.to_csv('restaurants_events.csv', index=False, encoding='utf-8-sig')