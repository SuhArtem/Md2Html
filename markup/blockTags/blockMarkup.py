
"""This file should contain the BlockMarkup class specific realization for block tags"""

from markup.markup import MarkUp
from markup.inlineTags.inlineMarkup import InlineMarkup

class BlockMarkup(InlineMarkup): # BlockMarkup shouldn't inherit from inlineMarkup class

    def __init__(self, elements: list[MarkUp] | MarkUp):
        super().__init__(elements)