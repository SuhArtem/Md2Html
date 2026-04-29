
"""This file should contain the BlockMarkup class specific realization for block tags"""
from typing import Union

from markup.markup import MarkUp
from markup.inlineTags.inlineMarkup import InlineMarkup

class BlockMarkup(InlineMarkup): # BlockMarkup shouldn't inherit from inlineMarkup class

    def __init__(self, elements: Union[list[MarkUp], MarkUp]):
        super().__init__(elements)