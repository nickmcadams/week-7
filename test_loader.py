import unittest
from loader import *

class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "Museum of Modern Art")

        self.assertIsNotNone(
            result,
            "A valid location should return location data."
        )

        self.assertEqual(
            result["location"],
            "Museum of Modern Art"
        )

        self.assertAlmostEqual(
            result["latitude"],
            40.7618552,
            delta=0.01
        )

        self.assertAlmostEqual(
            result["longitude"],
            -73.9782438,
            delta=0.01
        )

        self.assertEqual(
            result["type"],
            "museum"
        )

        result_alabama = fetch_location_data(
            geolocator,
            "USS Alabama Battleship Memorial Park"
        )

        self.assertIsNotNone(
            result_alabama,
            "USS Alabama Battleship Memorial Park should return location data."
        )

        self.assertAlmostEqual(
            result_alabama["latitude"],
            30.684373,
            delta=0.01
        )

        self.assertAlmostEqual(
            result_alabama["longitude"],
            -88.015316,
            delta=0.01
        )

        self.assertEqual(
            result_alabama["type"],
            "park"
        )

    def test_invalid_location(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")

        self.assertEqual(
            result["location"],
            "asdfqwer1234"
        )

        self.assertTrue(
            pd.isna(result["latitude"])
        )

        self.assertTrue(
            pd.isna(result["longitude"])
        )

        self.assertTrue(
            pd.isna(result["type"])
        )
if __name__ == "__main__":
    unittest.main()
