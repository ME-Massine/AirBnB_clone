#!/usr/bin/python3

"""Console Interface for the Application."""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def process_input(input_line):
    brace_check = re.search(r"\{(.*?)\}", input_line)
    bracket_check = re.search(r"\[(.*?)\]", input_line)
    if brace_check is None:
        if bracket_check is None:
            return [i.strip(",") for i in split(input_line)]
        else:
            lexer = split(input_line[:bracket_check.span()[0]])
            ret_l = [i.strip(",") for i in lexer]
            ret_l.append(bracket_check.group())
            return ret_l
    else:
        lexer = split(input_line[:brace_check.span()[0]])
        ret_l = [i.strip(",") for i in lexer]
        ret_l.append(brace_check.group())
        return ret_l


class AppConsole(cmd.Cmd):
    """The command interpreter for the application.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(app) "
    __model_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing when line is empty."""
        pass

    def default(self, input_line):
        """The default method invoked when input is not recognized"""
        command_set = {
            "all": self.all_handler,
            "show": self.show_handler,
            "destroy": self.destroy_handler,
            "count": self.count_handler,
            "update": self.update_handler
        }
        match = re.search(r"\.", input_line)
        if match is not None:
            input_tokens = [input_line[:match.span()[0]], input_line[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", input_tokens[1])
            if match is not None:
                command = [input_tokens[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in command_set.keys():
                    call = "{} {}".format(input_tokens[0], command[1])
                    return command_set[command[0]](call)
        print("*** Unknown syntax: {}".format(input_line))
        return False

    def do_quit(self, input_line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, input_line):
        """End of File signal to exit the program."""
        print("")
        return True

    def do_create(self, input_line):
        """Create a new class instance and print its id."""
        input_tokens = process_input(input_line)
        if len(input_tokens) == 0:
            print("** class name missing **")
        elif input_tokens[0] not in AppConsole.__model_classes:
            print("** class doesn't exist **")
        else:
            print(eval(input_tokens[0])().id)
            storage.save()

    def show_handler(self, input_line):
        """Display the string representation of a class instance of a given id."""
        input_tokens = process_input(input_line)
        object_dict = storage.all()
        if len(input_tokens) == 0:
            print("** class name missing **")
        elif input_tokens[0] not in AppConsole.__model_classes:
            print("** class doesn't exist **")
        elif len(input_tokens) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(input_tokens[0], input_tokens[1]) not in object_dict:
            print("** no instance found **")
        else:
            print(object_dict["{}.{}".format(input_tokens[0], input_tokens[1])])

    def destroy_handler(self, input_line):
        """Delete a class instance of a given id."""
        input_tokens = process_input(input_line)
        object_dict = storage.all()
        if len(input_tokens) == 0:
            print("** class name missing **")
        elif input_tokens[0] not in AppConsole.__model_classes:
            print("** class doesn't exist **")
        elif len(input_tokens) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(input_tokens[0], input_tokens[1]) not in object_dict.keys():
            print("** no instance found **")
        else:
            del object_dict["{}.{}".format(input_tokens[0], input_tokens[1])]
            storage.save()

    def all_handler(self, input_line):
        """Display string representations of all instances of a given class."""
        input_tokens = process_input(input_line)
        if len(input_tokens) > 0 and input_tokens[0] not in AppConsole.__model_classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(input_tokens) > 0 and input_tokens[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(input_tokens) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def count_handler(self, input_line):
        """Retrieve the number of instances of a given class."""
        input_tokens = process_input(input_line)
        count = 0
        for obj in storage.all().values():
            if input_tokens[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def update_handler(self, input_line):
        """Update a class instance of a given id."""
        input_tokens = process_input(input_line)
        object_dict = storage.all()

        if len(input_tokens) == 0:
            print("** class name missing **")
            return False
        if input_tokens[0] not in AppConsole.__model_classes:
            print("** class doesn't exist **")
            return False
        if len(input_tokens) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(input_tokens[0], input_tokens[1]) not in object_dict.keys():
            print("** no instance found **")
            return False
        if len(input_tokens) == 2:
            print("** attribute name missing **")
            return False
        if len(input_tokens) == 3 and not isinstance(eval(input_tokens[2]), dict):
            print("** value missing **")
            return False

        if len(input_tokens) == 4:
            obj = object_dict["{}.{}".format(input_tokens[0], input_tokens[1])]
            if input_tokens[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[input_tokens[2]])
                obj.__dict__[input_tokens[2]] = val_type(input_tokens[3])
            else:
                obj.__dict__[input_tokens[2]] = input_tokens[3]
        elif isinstance(eval(input_tokens[2]), dict):
            obj = object_dict["{}.{}".format(input_tokens[0], input_tokens[1])]
            for k, v in eval(input_tokens[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    val_type = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = val_type(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

if __name__ == "__main__":
    AppConsole().cmdloop()
