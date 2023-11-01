#!/usr/bin/python3
""" console for HBnB clone """


import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

