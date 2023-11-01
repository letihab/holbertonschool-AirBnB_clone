#!/usr/bin/python3
""" console for HBnB clone """


import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """definition of console"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        pass

    def check_args(self, args, num_args):
        if len(args) < num_args:
            return True
        return False

    def do_create(self, arg):
        """Create a new instance, save it to the JSON file, and print the id"""
        args = arg.split()
        if self.check_args(args, 1):
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name in storage.classes:
                new_instance = storage.classes[class_name]()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if self.check_args(args, 1):
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif self.check_args(args, 2):
            print("** instance id missing **")
        else:
            class_name = args[0]
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance"""
        args = arg.split()
        if self.check_args(args, 1):
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif self.check_args(args, 2):
            print("** instance id missing **")
        else:
            class_name = args[0]
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print the string representation of all instances"""
        args = arg.split()
        objects = []
        if not args:
            for obj in storage.all().values():
                objects.append(str(obj))
            print(objects)
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            for key, obj in storage.all().items():
                if key.split('.')[0] == args[0]:
                    objects.append(str(obj))
            print(objects)

    def do_update(self, arg):
        """Update an instance"""
        args = arg.split()
        if self.check_args(args, 1):
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif self.check_args(args, 2):
            print("** instance id missing **")
        else:
            class_name = args[0]
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            if key not in storage.all():
                print("** no instance found **")
            elif self.check_args(args, 3):
                print("** attribute name missing **")
            elif self.check_args(args, 4):
                print("** value missing **")
            else:
                instance = storage.all()[key]
                attr_name = args[2]
                attr_value = args[3]
                try:
                    attr_value = eval(attr_value)
                except (NameError, SyntaxError):
                    pass
                if hasattr(instance, attr_name):
                    if attr_name not in ["id", "created_at", "updated_at"]:
                        setattr(instance, attr_name, attr_value)
                        instance.save()
                    else:
                        print("** can't update id, created_at, or updated_at **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
