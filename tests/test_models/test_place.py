#!/usr/bin/env python3
"""Test model for Place class"""


import unittest
import os
from models.place import Place
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
import uuid


class TestPlace(unittest.TestCase):
    """Place model class test case"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.place = Place()
        cls.place.city_id = str(uuid.uuid4())
        cls.place.user_id = str(uuid.uuid4())
        cls.place.name = "Any place in the world"
        cls.place.description = "Suny Beatch"
        cls.place.number_rooms = 0
        cls.place.number_bathrooms = 0
        cls.place.max_guest = 0
        cls.place.price_by_night = 0
        cls.place.latitude = 0.0
        cls.place.longitude = 0.0
        cls.place.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()