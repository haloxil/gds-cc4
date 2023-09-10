## Assumptions and Interpretations

- Assume that populating empty values does not include the string 'Dummy'
- Assume that extracting the list of restaurants that have past events in April 2019 means that as long as April 2019 is within the event start date and event end date, we include that row of data. For example: if the event start date is 30-04-2019 and the event_end_date is 30-05-2019, we do not filter out this row of data.
- When determining the threshold for the different rating text based on aggregate rating, we find the minimum aggregate rating to be classified as that user text rating.
