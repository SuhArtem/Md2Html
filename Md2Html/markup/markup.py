
from abc import ABC, abstractmethod

class MarkUp(ABC):

    @abstractmethod
    def toHtml(self): ...

class TagMarkUp(MarkUp):

    @property
    @abstractmethod
    def tag(self): ...

    @property
    @abstractmethod
    def isNeedEndTag(self): ...