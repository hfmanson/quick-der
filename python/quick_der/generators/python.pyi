# Stubs for quick_der.generators.python (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from quick_der.generators import QuickDERgeneric
from typing import Any, Optional

class QuickDER2py(QuickDERgeneric):
    cursor_offset: Any = ...
    nested_typerefs: Any = ...
    nested_typecuts: Any = ...
    semamod: Any = ...
    refmods: Any = ...
    funmap_pytype: Any = ...
    def __init__(self, semamod, outfn, refmods) -> None: ...
    def comment(self, text): ...
    def generate_head(self): ...
    def generate_tail(self): ...
    def generate_values(self): ...
    def pygenValueAssignment(self, node): ...
    def pyvalInteger(self, valnode): ...
    def pyvalOID(self, valnode): ...
    def generate_classes(self): ...
    def pygenTypeAssignment(self, node): ...
    def generate_pytype(self, node, **subarg): ...
    unit: Any = ...
    def pytypeDefinedType(self, node, **subarg): ...
    def pytypeSimple(self, node, implicit_tag: Optional[Any] = ...): ...
    def pytypeTagged(self, node, implicit_tag: Optional[Any] = ...): ...
    def pytypeNamedType(self, node, **subarg): ...
    def pyhelpConstructedType(self, node): ...
    def pytypeChoice(self, node, implicit_tag: Optional[Any] = ...): ...
    def pytypeSequence(self, node, implicit_tag: str = ...): ...
    def pytypeSet(self, node, implicit_tag: str = ...): ...
    def pyhelpRepeatedType(self, node, dertag, recptag): ...
    def pytypeSequenceOf(self, node, implicit_tag: str = ...): ...
    def pytypeSetOf(self, node, implicit_tag: str = ...): ...
