from markup.inlineTags.inlineMarkup import InlineMarkup
from html import escape


class Binary(InlineMarkup):
    @property
    def isNeedEndTag(self):
        return True


class Emphasis(Binary):

    @property
    def tag(self):
        return "em"


class Paragraph(Binary):
    @property
    def tag(self):
        return 'p'


class Strikeout(Binary):
    @property
    def tag(self):
        return "s"


class Strong(Binary):
    @property
    def tag(self):
        return 'strong'


class Code(Binary):
    @property
    def tag(self):
        return "code"

    def toHtml(self):
        return (f"<{self.tag}>" +
                f"{escape(''.join([el.toHtml() for el in self.elements]))}" +
                f"{f'</{self.tag}>' if self.isNeedEndTag else ''}")


# shortcut binary tag name
BTN = {
    'em': Emphasis,
    'p': Paragraph,
    's': Strikeout,
    'strong': Strong,
    'code': Code
}
