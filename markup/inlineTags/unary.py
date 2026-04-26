from markup.inlineTags.inlineMarkup import InlineMarkup


class Unary(InlineMarkup):

    @property
    def isNeedEndTag(self):
        return False


class lineBreak(Unary):

    @property
    def tag(self):
        return "br"


# shortcut unary tag name
UTN = {
    'br': lineBreak
}
