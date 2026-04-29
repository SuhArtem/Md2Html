from enum import Enum, auto
from typing import Union

from Exeption.EOB import EndOfBuffer

class LexemeType(Enum):
    STRIKEOUT = auto()
    STRONG_DOWN = auto()
    EMPHASIS_DOWN = auto()
    CODE = auto()
    TEXT = auto()
    EOF = auto()
    DEFAULT = auto()
    SHIELD = auto()
    EMPHASIS_STAR = auto()
    STRONG_STAR = auto()
    HEADER = auto()
    PARAGRAPH = auto()
    SAMPLE = auto()


class Lexeme:
    type: LexemeType
    value: str

    def __init__(self, type: LexemeType, value: Union[str,int]):
        self.type = type
        self.value = value


class LexemeBuffer:

    def __init__(self, lexemes: list[Lexeme]):
        self.pos = 0
        self.lexemes = lexemes

    def next(self):
        el = self.current()
        self.forward()
        return el

    def back(self):
        self.pos -= 1

    def forward(self):
        self.pos += 1

    def current(self):
        if self.pos == len(self.lexemes):
            return None
        elif self.pos > len(self.lexemes):
            raise EndOfBuffer("Attempt to read data beyond the buffer limit")
        return self.lexemes[self.pos]

    def __len__(self):
        return len(self.lexemes)


class LexemeAnalyzer:
    _default_return_lexeme_value = -1

    def __init__(self, string):
        self.string = string
        self.specialSymbol = "-_*`\\!"

    def lexemeAnalise(self) -> list[Lexeme]:
        lexemes = []
        for k in range(1, 6 + 1): # from h1 to h6
            if self.string.startswith(f"{'#'*k} "):
                lexemes.append(Lexeme(LexemeType.HEADER, k))
                self.string = self.string[k + 1:]
                break
        else:
            lexemes.append(Lexeme(LexemeType.PARAGRAPH, LexemeAnalyzer._default_return_lexeme_value))

        i = 0
        while i < len(self.string):
            match self.string[i:i+2]:
                case "**":
                    lexemes.append(Lexeme(LexemeType.STRONG_STAR, self.string[i:i+2]))
                    i += 2
                    continue
                case "__":
                    lexemes.append(Lexeme(LexemeType.STRONG_DOWN, self.string[i:i+2]))
                    i += 2
                    continue
                case "--":
                    lexemes.append(Lexeme(LexemeType.STRIKEOUT, self.string[i:i+2]))
                    i += 2
                    continue
                case "!!":
                    lexemes.append(Lexeme(LexemeType.SAMPLE, self.string[i:i + 2]))
                    i += 2
                    continue
            match self.string[i]:
                case "\\":
                    lexemes.append(Lexeme(LexemeType.SHIELD, self.string[i]))
                    i += 1
                    continue
                case "*":
                    lexemes.append(Lexeme(LexemeType.EMPHASIS_STAR, self.string[i]))
                    i += 1
                    continue
                case "_":
                    lexemes.append(Lexeme(LexemeType.EMPHASIS_DOWN, self.string[i]))
                    i += 1
                    continue
                case "-":
                    lexemes.append(Lexeme(LexemeType.TEXT, self.string[i]))
                    i += 1
                    continue
                case "`":
                    lexemes.append(Lexeme(LexemeType.CODE, self.string[i]))
                    i += 1
                    continue
                case _:
                    text = []
                    while i < len(self.string) and self.string[i] not in self.specialSymbol:
                        text.append(self.string[i])
                        i += 1
                    lexemes.append((Lexeme(LexemeType.TEXT, ''.join(text))))

        lexemes.append(Lexeme(LexemeType.EOF, ''))
        return lexemes