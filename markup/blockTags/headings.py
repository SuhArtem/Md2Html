from typing import Union

from .blockMarkup import BlockMarkup
from ..markup import MarkUp


class Heading(BlockMarkup):
    _min_head_tag_size = 1
    _max_head_tag_size = 6
    _head_tags = dict([(i, f"h{i}") for i in range(_min_head_tag_size, _max_head_tag_size + 1)])

    def __init__(self, elements: Union[list[MarkUp], MarkUp], / , size=1):
        super().__init__(elements)
        self.size = size

    @property
    def isNeedEndTag(self):
        return True

    @property
    def tag(self):
        return self._head_tags[self.size]
