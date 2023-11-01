#!/usr/bin/python3
""" that serializes instances to a JSON file and deserializes JSON file to instances"""


import json


class FileStorage:
    """
    class that serializes instances
    to a json file and deserializes json
    file to instance
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
       """ serializes __objects to the JSON file (path: __file_path)"""
       data = {}
       for key, value in self.__objects.items():
           data[key] = value.to_dict()
           with open(self.__file_path, 'w', encoding='utf_8') as file:
            json.dump(data, file)

    def reload(self):
        """deserialize the json file to __objects"""
        try:
          with open(self.__file_path, 'r',  encoding='utf-8') as file:
            data = json.load(file)
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                from models.base_model import BaseModel
                self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
            


           



