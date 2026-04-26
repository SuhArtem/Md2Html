from markup.inlineTags.inlineMarkup import InlineMarkup


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


class Code(
    Binary):  # внутри кода весь текст теряет разметку, лучше его не наследовать от inlineMarkup и написать как отдельный класс либо всегда в нем хранить только текст
    @property
    def tag(self):
        return "code"


# shortcut binary tag name
BTN = {
    'em': Emphasis,
    'p': Paragraph,
    's': Strikeout,
    'strong': Strong,
    'code': Code
}
