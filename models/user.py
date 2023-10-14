#!/usr/bin/env python3
"""User Base model."""

from models.base_model import BaseModel


class User(BaseModel):
    """User base class."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
