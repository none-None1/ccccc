from pyparsing import *

chicken = CaselessKeyword("chicken")
chickens = Group(OneOrMore(chicken))
chicken_char = Group(Literal('"') + chickens + Literal('"'))
expr = Forward()
chicken_call = Group(chickens + Group("(" + Optional(DelimitedList(expr, ",")) + ")"))
expr <<= chicken_call | chicken_char | chickens
chicken_assignment = Group(
    chickens + ":" + (Group(chicken_call | chickens | chicken_char))
)
chicken_sentence = Group(Optional(chicken_assignment | chicken_call))
chicken_code = DelimitedList(chicken_sentence, ".", allow_trailing_delim=True)
__all__ = ["chicken_code"]
