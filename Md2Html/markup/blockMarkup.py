
"""This file should contain the BlockMarkup class specific realization for block tags"""

from .markup import MarkUp
from .inlineMarkup import inlineMarkup

class BlockMarkup(inlineMarkup): # BlockMarkup shouldn't inherit from inlineMarkup class

    def __init__(self, elements: list[MarkUp] | MarkUp):
        super().__init__(elements)