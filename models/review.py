#!/usr/bin/env python3
"""Review Base model."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review base class."""

    place_id = ""
    user_id = ""
    text = ""
