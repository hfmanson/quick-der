

class QuickDER2testdata(QuickDERgeneric):
    semamod: Any = ...
    refmods: Any = ...
    type2tdgen: Any = ...
    funmap_tdgen: Any = ...
    def __init__(self, semamod, outfn, refmods) -> None: ...
    def fetch_one(self, typename, casenr): ...
    def fetch_multi(self, typename, testcases): ...
    def all_typenames(self): ...
    def generate_testdata(self): ...
    def process_TypeAssignment(self, node): ...
    def generate_tdgen(self, node, **subarg): ...
    def tdgenDefinedType(self, node, **subarg): ...
    def der_prefixhead(self, tag, body): ...
    simple_cases: Any = ...
    def tdgenSimple(self, node): ...
    def tdgenNamedType(self, node, **subarg): ...
    nodeclass2basaltag: Any = ...
    def tdgenTagged(self, node, implicit_tag: Optional[Any] = ...): ...
    def tdgenChoice(self, node, implicit_tag: Optional[Any] = ...): ...
    def tdgenConstructed(self, node, implicit_tag: Optional[Any] = ...): ...
    def tdgenRepeated(self, node, **subarg): ...