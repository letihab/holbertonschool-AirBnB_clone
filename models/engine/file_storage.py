from json import dump, load
from models.base_model import BaseModel


# Create a dictionary to map class names to class objects
class_dict = {
    "BaseModel": BaseModel,
}

class FileStorage:
    ''' it defines the FileStorage Class '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' it returns the dictionary of all created objects '''
        return FileStorage.__objects

    def new(self, obj):
        '''
            it creates the dictionary of objects with
            key as the <class_name>.<obj_id> and
            value as the created object itself
        '''
        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        ''' it serializes the objects into JSON '''
        objects = FileStorage.__objects
        dict_from_obj = {key: obj.to_dict() for key, obj in objects.items()}

        with open(FileStorage.__file_path, 'w') as file:
            dump(dict_from_obj, file)

    def reload(self):
        ''' it deserializes JSON into objects '''
        try:
            with open(FileStorage.__file_path) as file:
                dict_from_json = load(file)
                for key, obj_dict in dict_from_json.items():
                    class_name = obj_dict['__class__']
                    obj_class = class_dict.get(class_name)
                    if obj_class:
                        obj = obj_class(**obj_dict)
                        self.new(obj)
        except Exception:
            return
