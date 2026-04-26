from markup.markup import MarkUp

class Text(MarkUp):

    def __init__(self, string: str):
        self.val = string

    def toHtml(self):
        return self.val