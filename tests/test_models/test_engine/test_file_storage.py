#!/usr/bin/env python3
"""Tests for the storage model."""

import unittest
import datetime
import os
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestStorageClass(unittest.TestCase):
    """Test storage class."""

    @classmethod
    def setUpClass(self):
        """Set test class."""
        self.storage = FileStorage()
        self.model_1 = BaseModel()
        self.model_2 = BaseModel()
        self.model_3 = BaseModel()
        self.model_4 = BaseModel()
        self.model_5 = BaseModel()
        self.model_6 = BaseModel()

        self.storage.reload()

    def test_0(self):
        """Check if the model key in the __objects when using new."""
        objects = self.storage.all()
        self.assertTrue(f"BaseModel.{self.model_1.id}" in objects)
        a = BaseModel()
        self.storage.new(a)
        self.assertTrue(f"BaseModel.{a.id}" in objects)

    def test_1(self):
        """Check the equality of the created model and the model."""
        objects = self.storage.all()
        self.assertEqual(objects[f"BaseModel.{self.model_1.id}"], self.model_1)
        self.assertEqual(objects[f"BaseModel.{self.model_2.id}"], self.model_2)
        self.assertEqual(objects[f"BaseModel.{self.model_3.id}"], self.model_3)

    def test_2(self):
        """Check if all method returning a dictionary."""
        objects = self.storage.all()
        self.assertTrue(type(objects) is dict)

    def test_3(self):
        """Check if the file exists after using the save method."""
        objects = self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_4(self):
        """Check if the models saved have same ids."""
        new_object = BaseModel()
        self.storage.new(new_object)
        self.storage.save()
        self.storage.reload()
        objects = self.storage.all()
        self.assertTrue(f"BaseModel.{new_object.id}" in self.storage.all())
        self.assertEqual(
            objects[f"BaseModel.{new_object.id}"].id, new_object.id
        )

    def test_5(self):
        """Test type storege."""
        self.assertEqual(type(models.storage), FileStorage)

    def test_6(self):
        """Test new None storage."""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

        with self.assertRaises(TypeError):
            models.storage.new()
