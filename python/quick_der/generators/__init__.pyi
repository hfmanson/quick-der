# Stubs for quick_der.generators (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class QuickDERgeneric:
    outfile: Any = ...
    comma1: Any = ...
    comma0: Any = ...
    def __init__(self, outfn, outext) -> None: ...
    def write(self, txt): ...
    def writeln(self, txt: str = ...): ...
    def newcomma(self, comma, firstcomma: str = ...): ...
    def comma(self): ...
    def getcomma(self): ...
    def setcomma(self, comma1, comma0): ...
    def close(self): ...