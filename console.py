#!/usr/bin/env python3
"""entry to the program
"""

import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    """Command-line interpreter class for HBNB project
    """

    # Prompt string
    prompt = "(hbnb) "

    # Dictionary mapping class names to their respective classes
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_create(self, line):
        """Create a new instance of a specified class and save it
        Usage: create <class name>
        """
        if not line:
            print("** class name missing **")
        else:
            if line not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            else:
                my_model = HBNBCommand.class_dict[line]()
                my_model.save()
                print(my_model.id)

    def do_show(self, line):
        """Print the string representation of an instance
        Usage: show <class name> <id>
        """
        key = self.get_object_key(line)
        if key:
            my_dict = storage.all()
            print(my_dict[key])

    def do_destroy(self, line):
        """Delete an instance based on the class name and id
        Usage: destroy <class name> <id>
        """
        key = self.get_object_key(line)
        if key:
            file_dict = storage.all()
            del file_dict[key]
            storage.save()

    def do_all(self, line):
        """Print string representations of objects
        Usage: all or all <class name>
        """
        my_dict = storage.all()
        my_list = []
        if len(line) == 0:
            for values in my_dict.values():
                my_list.append(str(values))
            print(my_list)
        else:
            if line not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            else:
                for value in my_dict.values():
                    if value.to_dict()["__class__"] == line:
                        my_list.append(str(value))
                print(my_list)

    def do_update(self, line):
        """Update an instance
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        my_list = self.parse(line)
        key = self.get_object_key(line)
        if key:
            if len(my_list) > 4:
                print("Usage: update <class name> <id> <attribute name>\
                    \"<attribute value>\"")
            elif len(my_list) == 3:
                print("** value missing **")
            elif len(my_list) == 2:
                print("** attribute name missing **")
            else:
                my_dict = storage.all()
                my_inst = my_dict[key]
                val = my_list[3][1:-1]
                try:
                    if "." in val:
                        val = float(val)
                    else:
                        val = int(val)
                except ValueError:
                    pass
                setattr(my_inst, my_list[2], val)
                storage.save()

    def do_EOF(self, line):
        """Command to end the program
        """
        return True

    def do_quit(self, line):
        """Command to end the program
        """
        return True

    def emptyline(self):
        pass

    def parse(self, arg):
        """Split a line into a list of arguments
        """
        return arg.split()

    def get_object_key(self, line):
        """Get the key of an object based on class name and id
        """
        my_list = self.parse(line)
        if len(my_list) == 0:
            print("** class name missing **")
        elif len(my_list) == 1:
            if my_list[0] not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(my_list) >= 2:
            if my_list[0] not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            else:
                key = f"{my_list[0]}.{my_list[1]}"
                file_dict = storage.all()
                if key in file_dict:
                    return key
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
