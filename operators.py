from enum import Enum
from nodes import *

def jump_label(target_name, program):
    index = list(map(lambda item: type(item) == label and item.name == target_name, program)).index(True)
    return {"R15" : int(index)}

def jumpt(condition, row_number):
    if condition:
        return {"R15" : int(row_number)-2}
    return {}

def jumpf(condition, row_number):
    if not condition:
        return {"R15" : int(row_number)-2}
    return {}

class operators(Enum):
    ADD = lambda a, b : a + b
    SUB = lambda a, b : a - b
    MUL = lambda a, b : a * b
    DIV = lambda a, b : a / b
    JMPT = jumpt
    JMPF = jumpf
    JMPL = jump_label