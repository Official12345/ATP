from enum import Enum
from nodes import *

def jump_label(target_name, program):
    index = list(map(lambda item: type(item) == label and item.name == target_name, program)).index(True)
    return {"PC" : int(index)}

def jumpt(condition, row_number):
    if condition:
        return {"PC" : int(row_number)-2}
    return {}

def jumpf(condition, row_number):
    if not condition:
        return {"PC" : int(row_number)-2}
    return {}

class operators(Enum):
    ADD = lambda a, b : a + b, "ADDITION"
    SUB = lambda a, b : a - b, "SUBTRACT"
    MUL = lambda a, b : a * b, "MULTIPLICATION"
    DIV = lambda a, b : a / b, "DIVISION"
    POW = lambda a, b : a ** b, "POWER"
    MOD = lambda a, b : a % b, "MODULUS"
    FDIV = lambda a , b : a // b, "FLOOR DIVISION"
    EQ = lambda a , b : a == b, "EQUALS"
    NEQ = lambda a , b : a != b, "NOT EQUALS"
    GRE = lambda a , b : a > b, "GREATER"
    GREEQ = lambda a , b : a >= b, "GREATER OR EQUALS"
    LES = lambda a , b : a < b, "LESSER"
    LESEQ = lambda a , b : a <= b, "LESSER OR EQUALS"
    JMPT = jumpt, "JUMP_TRUE"
    JMPF = jumpf, "JUMP_FALSE"
    JMPL = jump_label, "JUMP_LABEL"
    PRINT = lambda a : print(a), "PRINT"

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.__name__ = name
        return member