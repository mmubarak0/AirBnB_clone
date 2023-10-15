#!/usr/bin/env python3
"""Tests for the storage model."""

import unittest
import datetime
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
