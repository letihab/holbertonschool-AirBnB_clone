#!/usr/bin/python3
"""class for serialization and deserialization"""
import json
import os


class FileStorage :
    """class that serializes instances to a JSON file
    and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionnary"""
        return type(self).__objects

    def new(self, obj):
        """set new obj in __objects dictionary"""
        if obj.id in type(self.__objects):
            print("exists")
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """serializes __objects to the Json file __file_path"""
        new_dict = []
        for obj in type(self).__objects.values():
            new_dict.append(obj.to_dict())
        with open(type(self).__file_path, "w", encoding ='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """deserializes the jsonfile to __objects"""
        if os.path.exists(type(self).__file_path) is True:
            return
        try:
            with open(type(self).__file_path, "r") as file:
                new_obj = json.load(file)
                for key, value in new_obj.items():
                    obj = self.class_dict[value['__class__']](**value)
                    type(self).__objects[key] = obj
        except FileNotFoundError:
            pass
