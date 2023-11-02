#!/usr/bin/python3
"""defines unittest for base_model
unittest classes:
for instantiation
basemodel save and
dictionary
"""


import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """unittest for testing instantiation"""

    def test_no_args_instantiates(self):
        """instance of BaseModel without argument"""
        self.assertEqual(BaseModel, type(BaseModel()))
        """use assert to verify that the type of instantiation is BaseModel"""

    def test_new_instance_store(self):
        """verified is the new instance is store to an objects"""
        self.assertIn(BaseModel(), models.storage.all())

    def test_id_is_public_str(self):
        """check that the id attribute of an instance of
        Basemodel is a string and is public"""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public(self):
        """check if the attribut created_at is the type datetime"""
        self.assertEqual(datetime, type(BaseModel().created_at))

if __name__ == '__main__':
    unittest.main()    



