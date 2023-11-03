#!/usr/bin/python3
"""Defines unittests for models/city.py."""


from models import storage
import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel
import uuid
import os
from time import sleep


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.city = City()
        cls.city.state_id = str(uuid.uuid4())
        cls.city.name = "Laval"

    @classmethod
    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.city.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_state_id_is_public_class_attribute(self):
        ci = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(ci))
        self.assertNotIn("state_id", ci.__dict__)

    def test_name_is_public_class_attribute(self):
        ci = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(ci))
        self.assertNotIn("name", ci.__dict__)

    def test_attributes_are_string(self):
        self.assertIs(type(self.city.state_id), str)
        self.assertIs(type(self.city.name), str)

    def test_save(self):
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.city))

    def test_two_saves(self):
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        second_updated_at = cy.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cy.save()
        self.assertLess(second_updated_at, cy.updated_at)

    def test_to_dict_contains_correct_keys(self):
        cy = City()
        self.assertIn("id", cy.to_dict())
        self.assertIn("created_at", cy.to_dict())
        self.assertIn("updated_at", cy.to_dict())
        self.assertIn("__class__", cy.to_dict())

    def test_two_saves(self):
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        second_updated_at = cy.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cy.save()
        self.assertLess(second_updated_at, cy.updated_at)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        cy = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(cy.id, "345")
        self.assertEqual(cy.created_at, dt)
        self.assertEqual(cy.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()