import unittest
import pandas as pd
import sys
sys.path.append('src')
from restaurants import df_restaurants, metadata

class TestRestaurants(unittest.TestCase):
    def test_df_restaurants(self):
        self.assertIsInstance(df_restaurants, pd.DataFrame)
        self.assertGreater(len(df_restaurants), 0)
        self.assertListEqual(list(df_restaurants.columns), [
            'Restaurant Id',
            'Restaurant Name',
            'City',
            'Country',
            'User Rating Votes',
            'User Aggregate Rating',
            'Cuisines'
        ])

if __name__ == '__main__':
    unittest.main()