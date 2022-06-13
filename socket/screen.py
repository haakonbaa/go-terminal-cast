from curses import raw
from dataclasses import dataclass
import re

ANSIESC = re.compile(r'\x1b\[([0-9;\?]*[a-zA-Z]{1})')
@dataclass
class Action:
    action : str


class Terminal:
    def __init__(self, rows: int = 24, cols: int = 24, self.):
        self.rows = rows
        self.cols = cols
        self.cursorR = 0
        self.cursorC = 0

    def print_raw():
        pass

    def print(self, text):
        index = 0
        textAction = []
        escCodes = [*ANSIESC.finditer(text)]
        for m in escCodes:
            if not m.start() == index:
                textAction.append(text[index:m.start()])
            textAction.append(Action(m.string[m.start()+2:m.end()]))
            index = m.end()
        if not index == len(text):
            textAction.append(text[index:])
        for tora in textAction:
            if isinstance(tora,Action):
                self.do_action(tora)
            else:
                self.print_raw(tora)

    
    def do_action(self, action : str):
        # :TODO action
        print(action)

t = Terminal()
t.print('\x1b[31mDette er en \x1b[32mtest\x1b[0m')

__all__ = ['Terminal']
