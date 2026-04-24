from ..inlineMarkup import inlineMarkup


class Emphasis(inlineMarkup):

    @property
    def tag(self):
        return "em"

    @property
    def isNeedEndTag(self):
        return True


class Paragraph(inlineMarkup):
    @property
    def tag(self):
        return 'p'
    @property
    def isNeedEndTag(self):
        return True


class Strikeout(inlineMarkup):
    @property
    def tag(self):
        return "s"

    @property
    def isNeedEndTag(self):
        return True


class Strong(inlineMarkup):
    @property
    def tag(self):
        return 'strong'

    @property
    def isNeedEndTag(self):
        return True


class Code(inlineMarkup): # внутри кода весь текст теряет разметку, лучше его не наследовать от inlineMarkup и написать как отдельный класс либо всегда в нем хранить только текст
    @property
    def tag(self):
        return "code"

    @property
    def isNeedEndTag(self):
        return True

# shortcut binary tag name
BTN = {
    'em': Emphasis,
    'p': Paragraph,
    's': Strikeout,
    'strong': Strong,
    'code': Code
}