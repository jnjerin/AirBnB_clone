#!/usr/bin/python3
""" City Module for airbnb project """
from models.base_model import BaseModel


class City(BaseModel):
    """ This class defines the city to look for """
    state_id = ""
    name = ""
