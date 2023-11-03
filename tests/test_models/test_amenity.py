#!/usr/bin/env python3
"""Unittest module for the Amenity Class."""

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
import models
from time import sleep

class TestAmenity(unittest.TestCase):
    """Amenity model class test case"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.amenity = Amenity()
        cls.amenity.name = "Wifi"

    @classmethod
    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass 

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel))

    a = Amenity()
    def test_has_attributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))

    def test_attributes_are_string(self):
        self.assertIs(type(self.amenity.name), str)

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = Amenity.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_save(self):
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.amenity))

    def test_str_representation(self):
        dt = datetime.now()
        dt_repr = repr(dt)
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        amstr = am.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    
    def test_to_dict_datetime_attributes_are_strs(self):
        am = Amenity()
        am_dict = am.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), tdict)

    def test_two_saves(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        second_updated_at = am.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        am.save()
        self.assertLess(second_updated_at, am.updated_at)

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_two_amenities_unique_ids(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_two_amenities_different_created_at(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_two_amenities_different_updated_at(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)


if __name__ == "__main__":
    unittest.main()