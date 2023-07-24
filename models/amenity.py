#!/usr/bin/python3
""" Amenity Module for airbnb project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines amenities that user can choose from to offer at their place"""
    name = ""
