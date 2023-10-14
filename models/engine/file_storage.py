#!/usr/bin/env python3
"""Storage module."""

import json
import os
import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        storage = FileStorage.__objects
        storage[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        storage = FileStorage.__objects
        storage_as_dict = {}
        for key in storage.keys():
            storage_as_dict[key] = storage[key].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(storage_as_dict))

    def reload(self):
        """Deserialize the JSON file to __objects."""
        storage = FileStorage.__objects
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                storage = json.loads(f.read())
                for key, value in storage.items():
                    name = value["__class__"]
                    self.new(eval(name)(**value))
