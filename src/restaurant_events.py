"""
This module extracts selected fields and
store the data as restaurant_events.csv.
"""
from datetime import datetime, date, timedelta
import pandas as pd
import main
from utils import populate_empty_values

df_restaurants, metadata = main.main()

year = metadata['rules']['date'][0]
month = metadata['rules']['date'][1]
day = metadata['rules']['date'][2]

restaurant_id = metadata['restaurant_id']
restaurant_name = metadata['restaurant_name']
photo_url = metadata['photo_url']
events = metadata['events']['key']
event_id = metadata['events']['event_id'].split('.')[1]
event_title = metadata['events']['event_title'].split('.')[1]
event_start_date = metadata['events']['event_start_date'].split('.')[1]
event_end_date = metadata['events']['event_end_date'].split('.')[1]

df_events = df_restaurants[[restaurant_id, restaurant_name,
                            photo_url, events]]
df_events = df_events.dropna(subset=[events])
df_events = df_events.explode(events).reset_index(drop=True)

fields_to_extract = [event_id, event_title, event_start_date, event_end_date]
for field in fields_to_extract:
    df_events[field] = df_events[events].apply(lambda x: x['event'][field])

df_events[event_start_date] = pd.to_datetime(df_events[event_start_date])
df_events[event_end_date] = pd.to_datetime(df_events[event_end_date])

df_events = df_events[(df_events[event_start_date]
                       <= datetime.combine(
                           date(year, month + 1, day),
                           datetime.min.time()) - timedelta(days=1))
                      & (df_events[event_end_date]
                         >= datetime.combine(
                             date(year, month, day),
                             datetime.min.time()))]

df_events = populate_empty_values(df_events)

df_events = df_events.rename(columns={
    event_id: 'Event Id',
    restaurant_id: 'Restaurant Id',
    restaurant_name: 'Restaurant Name',
    photo_url: 'Photo URL',
    event_title: 'Event Title',
    event_start_date: 'Event Start Date',
    event_end_date: 'Event End Date'
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
