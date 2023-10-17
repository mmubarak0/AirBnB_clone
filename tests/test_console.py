#!/usr/bin/env python3
"""Tests for the base model."""

import unittest
import datetime
import os
from models.base_model import BaseModel
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestBaseClass(unittest.TestCase):
    """Test base class."""

    @classmethod
    def setUpClass(self):
        """Set test class."""
        self.model_1 = BaseModel()
        self.model_2 = BaseModel()

    def test_0(self):
        """Test help method."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            help_txt = """Used to Exit the interactive console"""
            self.assertNotEqual(help_txt, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            help_txt = """all [<ModelName>]
            Prints all string representation of all instances
            based or not on the class name. Ex:
            (hbnb) all BaseModel
            or
            (hbnb) all
            """
            self.assertNotEqual(help_txt, f.getvalue())

    def test_1(self):
        """Test show method."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {self.model_1.id}")
            # match the [<class name>] part
            s = r"\[\w*\]\s"
            # match (<self.id>) part
            s += r"\([a-z0-9]+-[a-z0-9]+-[a-z0-9]+-[a-zA-Z0-9]+-[a-z0-9]+\)\s"
            # match <self.__dict__> part
            s += r"{[^}]*}"
            self.assertRegex(f.getvalue(), s)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {self.model_2.id}")
            # match the [<class name>] part
            s = r"\[\w*\]\s"
            # match (<self.id>) part
            s += r"\([a-z0-9]+-[a-z0-9]+-[a-z0-9]+-[a-zA-Z0-9]+-[a-z0-9]+\)\s"
            # match <self.__dict__> part
            s += r"{[^}]*}"
            self.assertRegex(f.getvalue(), s)

    def test_2(self):
        """Test all method."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all")
            if os.path.isfile("file.json"):
                self.assertTrue(len(f.getvalue()) > 0)
                self.assertEqual(f.getvalue()[0], "[")
                self.assertEqual(f.getvalue()[-2], "]")
            else:
                self.assertEqual("", f.getvalue())
