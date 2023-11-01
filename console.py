#!/usr/bin/python3
""" console HBNBcommand for manage file of HBNB project"""


import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ definition of HBnB console"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to the JSON file"""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances or instances of a specific class"""
        args = arg.split()
        objects = []
        if len(args) == 0:
            for obj in storage.all().values():
                objects.append(str(obj))
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        else:
            for key, obj in storage.all().items():
                if key.split('.')[0] == args[0]:
                    objects.append(str(obj))
        print(objects)

    def do_update(self, arg):
        """Updates an instance's attribute"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                instance = storage.all()[key]
                attribute_name = args[2]
                attribute_value = args[3]
                try:
                    attribute_value = eval(attribute_value)
                except (NameError, SyntaxError):
                    pass
                setattr(instance, attribute_name, attribute_value)
                instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
