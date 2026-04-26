from enum import Enum

from Exeption.EOB import EndOfBuffer

class LexemeType(Enum):
    STRIKEOUT = 1
    STRONG_DOWN = 2
    EMPHASIS_DOWN = 3
    CODE = 4
    TEXT = 5
    EOF = 6
    DEFAULT = 7
    SHIELD = 8
    EMPHASIS_STAR = 9
    STRONG_STAR = 10


class Lexeme:
    type: LexemeType
    value: str

    def __init__(self, type: LexemeType, value: str):
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

    def __init__(self, string):
        self.string = string

    def lexemeAnalise(self) -> list[Lexeme]:
        lexemes = []
        i = 0
        while i < len(self.string):
            match self.string[i]:
                case "\\":
                    lexemes.append(Lexeme(LexemeType.SHIELD, self.string[i]))
                    i += 1
                    continue
                case "*":
                    if i + 1 < len(self.string) and self.string[i + 1] == "*":
                        lexemes.append(Lexeme(LexemeType.STRONG_STAR, self.string[i] + self.string[i + 1]))
                        i += 2
                    else:
                        lexemes.append(Lexeme(LexemeType.EMPHASIS_STAR, self.string[i]))
                        i += 1
                        continue
                case "_":
                    if i + 1 < len(self.string) and self.string[i + 1] == "_":
                        lexemes.append(Lexeme(LexemeType.STRONG_DOWN, self.string[i] + self.string[i + 1]))
                        i += 2
                    else:
                        lexemes.append(Lexeme(LexemeType.EMPHASIS_DOWN, self.string[i]))
                        i += 1
                        continue
                case "-":
                    if i + 1 < len(self.string) and self.string[i + 1] == "-":
                        lexemes.append(Lexeme(LexemeType.STRIKEOUT, self.string[i] + self.string[i + 1]))
                        i += 2
                    else:
                        lexemes.append(Lexeme(LexemeType.TEXT, self.string[i]))
                        i += 1
                        continue
                case "`":
                    lexemes.append(Lexeme(LexemeType.CODE, self.string[i]))
                    i += 1
                    continue

            text = []
            while i < len(self.string) and self.string[i] not in "`-_*\\": # сюда как раз код можно внести
                text.append(self.string[i])
                i += 1
            lexemes.append((Lexeme(LexemeType.TEXT, ''.join(text))))

        lexemes.append(Lexeme(LexemeType.EOF, ''))
        return lexemes
