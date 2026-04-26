
from typing import Union

from markup.markup import MarkUp, TagMarkUp


class InlineMarkup(TagMarkUp):

    def __init__(self, elements: Union[list[MarkUp], MarkUp]):
        self.elements: list[MarkUp]
        if isinstance(elements, MarkUp):
            self.elements = [elements]
        else:
            self.elements = elements

    def toHtml(self):
        return f"<{self.tag}>{''.join([el.toHtml() for el in self.elements])}{f'</{self.tag}>' if self.isNeedEndTag else ''}"

    def add(self, el: MarkUp):
        self.elements.append(el)