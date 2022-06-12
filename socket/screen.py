from curses import raw
import re

ANSIESC = re.compile(r'\x1b\[([0-9;\?]*[a-zA-Z]{1})')

class Terminal:
    def __init__(self, rows : int = 24, cols : int = 24):
        self.rows = rows
        self.cols = cols
        self.cursorR = 0
        self.cursorC = 0
    
    def print(self, text):
        index = 0
        rawText = []
        for m in ANSIESC.finditer(text):
            if not m.start() == index:
                rawText.append(text[index:m.start()])
            index = m.end()
        if not index == len(text):
            rawText.append(text[index:len(rawText)])
        print(rawText)
        

t = Terminal()
t.print('\x1b[31mDette er en \x1b[32mtest\x1b[0m')

__all__ = ['Terminal']