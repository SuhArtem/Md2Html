
from markup.markup import MarkUp
from markup.inlineTags.unary import *
from markup.inlineTags.binary import *
from markup.blockTags.headings import *
from markup.text import Text
from handlers.lexemAnalzer import *


class Md2Html:

    def __init__(self, inputFile, outputFile):
        self.inputFile = inputFile
        self.outputFile = outputFile
        self.strings: list[str] = []
        self.htmlStrings: list[MarkUp] = []

    def _read(self):
        """This read method realization makes text block,
            separated from the other blocks by new line, contains in one tag"""

        with open(self.inputFile, 'r', encoding='utf-8') as file:
            strseq = []
            for string in file.readlines() + ['\n']:
                if string != '\n':
                    strseq.append(string)
                else:
                    el = ''.join(strseq).rstrip()
                    if el:
                        self.strings.append(el)
                    strseq = []

    def _write(self):
        with open(self.outputFile, 'w', encoding='utf-8') as file:
            for string in self.htmlStrings:
                file.write(string.toHtml())

    def toHtml(self):
        self._read()

        for string in self.strings:
            if string != '\n':
                self.htmlStrings += [self._handler(LexemeBuffer(LexemeAnalyzer(string).lexemeAnalise()))] + [Text('\n')]

        self._write()

    def _handler(self, lexemes: LexemeBuffer) -> MarkUp:
        wrap = lexemes.next()
        if wrap.type == LexemeType.HEADER:
            return Heading(self._string_handler(lexemes), size=wrap.value)
        elif wrap.type == LexemeType.PARAGRAPH:
            return Paragraph(self._string_handler(lexemes))
        return Text('')

    def _string_handler(self, lexemes: LexemeBuffer, last_tag: Lexeme = Lexeme(LexemeType.DEFAULT, '')) -> list[MarkUp]:
        lexeme = lexemes.next()
        mark = []
        while lexeme:
            if lexeme.type == last_tag.type or lexeme.type == LexemeType.EOF:
                lexemes.back()
                break
            elif lexeme.type == LexemeType.TEXT:
                return mark + [Text(lexeme.value)] + self._string_handler(lexemes, last_tag)
            elif lexeme.type == LexemeType.SHIELD:
                mark.append(Text(lexemes.next().value))
            else:
                val = self._string_handler(lexemes, lexeme)
                if lexemes.current().type == lexeme.type:
                    if lexeme.type == LexemeType.STRIKEOUT:
                        mark.append(Strikeout(val))
                    elif lexeme.type == LexemeType.CODE:
                        mark.append(Code(val))
                    elif lexeme.type == LexemeType.SAMPLE:
                        mark.append(Sample(val))
                    elif lexeme.type == LexemeType.STRONG_STAR or lexeme.type == LexemeType.STRONG_DOWN:
                        mark.append(Strong(val))
                    elif lexeme.type == LexemeType.EMPHASIS_STAR or lexeme.type == LexemeType.EMPHASIS_DOWN:
                        mark.append(Emphasis(val))
                    lexemes.forward()
                else:
                    mark.append(Text(lexeme.value))
                    mark += val


            lexeme = lexemes.next()
        return mark