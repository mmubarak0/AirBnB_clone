#!/usr/bin/env python3
"""Console program."""

import cmd
import shlex
import models
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Base class inherented from cmd module."""

    prompt = "(hbnb) "
    _classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    ]

    # ---------------------------- Cmd commands ------------------------------
    def emptyline(self):
        """Take care of empty line."""
        pass

    def default(self, s):
        """Take care of unrecognized commands."""
        line = shlex.split(s)
        match = re.search(r"([A-Z]\w*)\.(\w+)\(\w*\)", line[0])
        if match:
            class_name = match.group(1)
            objects = models.storage.all()
            if class_name in HBNBCommand._classes:
                command = match.group(2)
                if command == "all":
                    self.do_all(class_name)
                if command == "count":
                    result = 0
                    for key, model in objects.items():
                        if key.startswith(class_name):
                            result += 1
                    print(result)
            else:
                print("** class doesn't exist **")
        else:
            return cmd.Cmd.default(self, s)

    # --------------------------- Main commands ------------------------------
    def do_create(self, s):
        """Create a new instance of BaseModel."""
        line = shlex.split(s)
        n = len(line)
        if n:
            class_name = line[0]
            if class_name not in HBNBCommand._classes:
                print("** class doesn't exist **")
            else:
                new_model = eval(class_name)()
                models.storage.new(new_model)
                models.storage.save()
                print(new_model.id)
        else:
            print("** class name missing **")

    def do_show(self, s):
        """Print string representation of instance based on class name."""
        line = shlex.split(s)
        n = len(line)
        if n:
            class_name = line[0]
            if class_name not in HBNBCommand._classes:
                print("** class doesn't exist **")
            else:
                if n < 2:
                    print("** instance id missing **")
                else:
                    objects = models.storage.all()
                    id = line[1]
                    if f"{class_name}.{id}" not in objects:
                        print("** no instance found **")
                    else:
                        print(objects[f"{class_name}.{id}"])
        else:
            print("** class name missing **")

    def do_destroy(self, s):
        """Delete an instance based on the class name and id."""
        line = shlex.split(s)
        n = len(line)
        if n:
            class_name = line[0]
            if class_name not in HBNBCommand._classes:
                print("** class doesn't exist **")
            else:
                if n < 2:
                    print("** instance id missing **")
                else:
                    objects = models.storage.all()
                    id = line[1]
                    if f"{class_name}.{id}" not in objects:
                        print("** no instance found **")
                    else:
                        del objects[f"{class_name}.{id}"]
                        models.storage.save()
        else:
            print("** class name missing **")

    def do_all(self, s):
        """Print all string representation of all instances."""
        line = shlex.split(s)
        n = len(line)
        objects = models.storage.all()
        result = []
        if n:
            class_name = line[0]
            if class_name not in HBNBCommand._classes:
                print("** class doesn't exist **")
            else:
                for key, model in objects.items():
                    if key.startswith(class_name):
                        result.append(str(model))
        else:
            for key, model in objects.items():
                result.append(str(model))
        if result:
            print(result)

    def do_update(self, s):
        """Update an instance based on the class name and id."""
        line = shlex.split(s)
        n = len(line)
        if n:
            class_name = line[0]
            if class_name not in HBNBCommand._classes:
                print("** class doesn't exist **")
            else:
                if n < 2:
                    print("** instance id missing **")
                else:
                    objects = models.storage.all()
                    id = line[1]
                    if f"{class_name}.{id}" not in objects:
                        print("** no instance found **")
                    else:
                        if n < 3:
                            print("** attribute name missing **")
                        else:
                            attr = line[2]
                            if n < 4:
                                print("** value missing **")
                            else:
                                value = line[3]
                                dont_touch = ["id", "created_at", "updated_at"]
                                if attr not in dont_touch:
                                    model = objects[f"{class_name}.{id}"]
                                    if hasattr(model, attr):
                                        t = type(getattr(model, attr))
                                        setattr(model, attr, t(value))
                                    else:
                                        setattr(model, attr, value)
                                    model.save()
        else:
            print("** class name missing **")

    def do_quit(self, line):
        """End of input stream."""
        return True

    def do_EOF(self, line):
        """End of input stream."""
        print()
        return True

    # --------------------------- Help commands ------------------------------
    def help_quit(self):
        """Help quit."""
        help_txt = """Used to Exit the interactive console"""
        print(help_txt)

    def help_create(self):
        """Help on create command."""
        help_txt = """create <ModelName>
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex:
        (hbnb) create BaseModel
        """
        print(help_txt)

    def help_show(self):
        """Help on show command."""
        help_txt = """show <ModelName> <id>
        Prints the string representation of an instance
        based on the class name and id.
        Ex:
        (hbnb) show BaseModel 1234-1234-1234
        """
        print(help_txt)

    def help_all(self):
        """Help on all command."""
        help_txt = """all [<ModelName>]
        Prints all string representation of all instances
        based or not on the class name. Ex:
        (hbnb) all BaseModel
        or
        (hbnb) all
        """
        print(help_txt)

    def help_destroy(self):
        """Help on destroy command."""
        help_txt = """destroy <BaseModel> <id>
        Deletes an instance
        based on the class name and id (save the change into the JSON file).
        Ex:
        (hbnb) destroy BaseModel 1234-1234-1234
        """
        print(help_txt)

    def help_update(self):
        """Help on update command."""
        help_txt = """update <BaseModel> <id> <attr name> <attr value>
         Updates an instance
         based on the class name and id by adding or updating attribute
         (save the change into the JSON file). Ex:
         (hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        print(help_txt)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
