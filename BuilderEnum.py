from enum import Enum

class BuilderEnum(Enum):
    #del lenguaje
    SYMBOL = "symbol"
    KLEENE = "*"
    PLUS = "+"
    OR = "|"
    LEFT_PARENS = "("
    RIGHT_PARENS = ")"