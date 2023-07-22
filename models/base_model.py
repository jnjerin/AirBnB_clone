#!/usr/bin/python3
"""This module defines a base class for all models in our airbnb clone"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods
    """
    def __init__(self, *args, **kwargs):
