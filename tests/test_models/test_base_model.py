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

    def test_id_is_public_str(self):
        """check that the id attribute of an instance of
        Basemodel is a string and is public"""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public(self):
        """check if the attribut created_at is the type datetime"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_model_unique_id(self):
        """check if id is unique"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_two_models_different_created_at(self):
        """checks wether the creation timestamps are #"""
        b1 = BaseModel()
        sleep(0.05)
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)

    def test_two_models_different_updated_at(self):
        b1 = BaseModel()
        sleep(0.05)
        b2 = BaseModel()
        self.assertLess(b1.updated_at, b2.updated_at)

    def test_str_representation(self):
        """check if str correctly generated a string representation"""
        dh = datetime.today()
        dh_repr = repr(dh)
        bm = BaseModel()
        bm.id = "123457"
        bm.created_at = bm.updated_at = dh
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123457)", bmstr)
        self.assertIn("'id': '123457'", bmstr)
        self.assertIn("'created_at': " + dh_repr, bmstr)
        self.assertIn("'updated_at': " + dh_repr, bmstr)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """check if key value instantiation work correctly"""
        dh = datetime.today()
        dh_iso = dh.isoformat()
        bm = BaseModel(id="500", created_at=dh_iso, updated_at=dh_iso)
        self.assertEqual(bm.id, "500")
        self.assertEqual(bm.created_at, dh)
        self.assertEqual(bm.updated_at, dh)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dh = datetime.today()
        dh_iso = dh.isoformat()
        bm = BaseModel("12", id="500", created_at=dh_iso, updated_at=dh_iso)
        self.assertEqual(bm.id, "500")
        self.assertEqual(bm.created_at, dh)
        self.assertEqual(bm.updated_at, dh)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save(self):
        """check if datetime is update correctly"""
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_many_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)

    def test_to_dict_output(self):
        dh = datetime.today()
        bm = BaseModel()
        bm.id = "123457"
        bm.created_at = bm.updated_at = dh
        tdict = {
            'id': '123457',
            '__class__': 'BaseModel',
            'created_at': dh.isoformat(),
            'updated_at': dh.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

  
if __name__ == '__main__':
    unittest.main()    



