import unittest
import sys
sys.path.append('src')
from main import main
import pandas as pd

class TestMain(unittest.TestCase):
    def test_main(self):
        df, metadata = main()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsInstance(metadata, dict)
        self.assertGreater(len(df), 0)
        self.assertGreater(len(metadata), 0)

if __name__ == '__main__':
    unittest.main()