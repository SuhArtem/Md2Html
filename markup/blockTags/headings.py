from .blockMarkup import BlockMarkup


class heading(BlockMarkup):

    @property
    def isNeedEndTag(self):
        return True


class H1(heading):  # TODO: All of thees H{i} class should be in one class
    @property
    def tag(self):
        return "h1"


class H2(heading):
    @property
    def tag(self):
        return "h2"


class H3(heading):
    @property
    def tag(self):
        return "h3"


class H4(heading):
    @property
    def tag(self):
        return "h4"


class H5(heading):
    @property
    def tag(self):
        return "h5"


class H6(heading):
    @property
    def tag(self):
        return "h6"
