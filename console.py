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

    def do_help(self, arg):
        """Show help for a specific command or list available commands"""
        if arg:
            # If the user provides a command as an argument, display help for that command.
            super().do_help(arg)
        else:
            # If no argument is provided, display a list of available commands.
            super().do_help(arg=None)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

