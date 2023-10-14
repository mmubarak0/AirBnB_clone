#!/usr/bin/env python3
"""Base model of objects."""

import uuid
import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize the model."""
        __now = datetime.datetime.now()
        if len(kwargs) > 0:
            for key in kwargs:
                if key != "__class__":
                    setattr(self, key, kwargs[key])
            self.id = kwargs.get("id", str(uuid.uuid4()))
            self.created_at = datetime.datetime.fromisoformat(
                        kwargs.get("created_at", __now.isoformat())
                )
            self.updated_at = datetime.datetime.fromisoformat(
                        kwargs.get("updated_at", __now.isoformat())
                )
        else:
            self.id = str(uuid.uuid4())
            self.created_at = __now
            self.updated_at = __now
            models.storage.new(self)

    def __str__(self):
        """Str represntation of the model."""
        return f"[{str(self.__class__.__name__)}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__."""
        res = {}
        for key in self.__dict__:
            res[key] = self.__dict__[key]
        res["__class__"] = str(self.__class__.__name__)
        res["created_at"] = res["created_at"].isoformat()
        res["updated_at"] = res["updated_at"].isoformat()
        return res
