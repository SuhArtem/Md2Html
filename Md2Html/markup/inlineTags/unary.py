from markup.blockMarkup import BlockMarkup

class lineBreak(BlockMarkup):

    @property
    def tag(self):
        return "br"

    @property
    def isNeedEndTag(self):
        return False

#shortcut unary tag name
UTN = {
    'br': lineBreak
}