from typing import Any

from markup.markup import MarkUp
from markup.inlineTags.unary import *
from markup.inlineTags.binary import BTN
from markup.blockTags.headings import *
from markup.text import Text
from handlers.lexemAnalzer import *


class Md2Html:

    def __init__(self, inputFile, outputFile):
        self.inputFile = inputFile
        self.outputFile = outputFile
        self.strings: list[str] = []
        self.htmlStrings: list[MarkUp] = []

    # def _read(self):
    #     with open(self.inputFile, 'r', encoding='utf-8') as file:
    #         strings = file.readlines()
    #
    #         st = ''  # В питоне строки не изменяемые TODO: использовать list с join по необходимости
    #         for string in strings:
    #             if string != '\n':  # <br>
    #                 st += string
    #             else:
    #                 if st != '':
    #                     st = st.rstrip()
    #                     self.strings.append(st)
    #                 st = ''  # повторяющийся код с 22 строкой (МОЖНО БЕЗ НЕГО)
    #         if st != '':  # повторяющийся код с 27 строкой (МОЖНО БЕЗ НЕГО)
    #             st = st.rstrip()
    #             self.strings.append(st)
    #         # self.strings = [i.rstrip() for i in file.readline() if i != '\n']

    def _read(self):
        """This read method realization makes text block,
            separated from the other blocks by new line, contains in one tag"""

        with open(self.inputFile, 'r', encoding='utf-8') as file:
            strseq = []
            for string in file.readlines():
                if string != '\n':
                    strseq.append(string)
                else:
                    self.strings.append(''.join(strseq).rstrip())
                    strseq = []

    def _write(self):
        with open(self.outputFile, 'w', encoding='utf-8') as file:
            for string in self.htmlStrings:
                file.write(string.toHtml())

    def toHtml(self):
        self._read()

        for string in self.strings:
            if string != '\n':
                self.htmlStrings += [self.handler(LexemeBuffer(LexemeAnalyzer(string).lexemeAnalise()))] + [Text('\n')]

        self._write()

    def handler(self, lexemes: LexemeBuffer) -> MarkUp:
        wrap = BTN['p']

        firstString = lexemes.next()  # TODO: Move this code block to the LexemeAnalyzer
        if firstString.type == LexemeType.TEXT:
            if firstString.value.startswith("# "):
                wrap = H1
                firstString.value = firstString.value[2:]
            elif firstString.value.startswith("## "):
                wrap = H2
                firstString.value = firstString.value[3:]
            elif firstString.value.startswith("### "):
                wrap = H3
                firstString.value = firstString.value[4:]
            elif firstString.value.startswith("#### "):
                wrap = H4
                firstString.value = firstString.value[5:]
            elif firstString.value.startswith("##### "):
                wrap = H5
                firstString.value = firstString.value[6:]
            elif firstString.value.startswith("###### "):
                wrap = H6
                firstString.value = firstString.value[7:]
        lexemes.back()

        return wrap(self._string_handler(lexemes))

    def _string_handler(self, lexemes: LexemeBuffer, last_sign: Lexeme = Lexeme(LexemeType.DEFAULT, '')) -> list[MarkUp]:
        lexeme = lexemes.next()
        mark = []
        while lexeme:
            if lexeme.type == last_sign.type:
                break
            match lexeme.type:
                case LexemeType.TEXT:
                    return mark + [Text(lexeme.value)] + self._string_handler(lexemes, last_sign)
                case LexemeType.CODE:
                    mark.append(BTN['code'](self._string_handler(lexemes, lexeme)))
                case LexemeType.STRIKEOUT:
                    mark.append(BTN['s'](self._string_handler(lexemes, lexeme)))
                case LexemeType.STRONG:
                    mark.append(BTN['strong'](self._string_handler(lexemes, lexeme)))
                case LexemeType.EMPHASIS:
                    mark.append(BTN['em'](self._string_handler(lexemes, lexeme)))
                case LexemeType.EOF:
                    lexemes.back()
                    break

            lexeme = lexemes.next()
        return mark