from operators import *
from nodes import *
from typing import Callable

Program_state = {"R0": 0, "R1": 0, "R2": 0, "R3": 0, "R4": 0, "R5": 0, "R6": 0, "R7": 0, "R8": 0, "R9": 0, "R10": 0, "R11": 0, "R12": 0, "R13": 0, "R14": 0, "PC": 0, }

def Read_file_into_lines(filename) -> [str]:
    file = open(filename, "r")
    return file.read().splitlines()

def Lines_into_operations(Lines : [str]) -> [operator_node]:
    return list(map(Line_to_operation, Lines))

def Check_reg(name : str):# -> Union[int, str]:
    if(name.isdigit()):
        return int(name)
    elif (name[0] == '-' and name[1:].isdigit()):
        return int(name)
    else:
        return name
        
def Check_reg2(name : str, Program_state : dict):# -> Union[int, str]:
    if(type(name) == int):
        return name
    else:
        return Program_state.get(name)

def Line_to_operation(line : str) -> operator_node:
    line = line.split()
    if line[0] == "\n":
        return None
    elif line[0] == "ADD":
        return operator_node(operators.ADD, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "SUB":
        return operator_node(operators.SUB, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "MUL":
        return operator_node(operators.MUL, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "STR":
        return operator_node(operators.ADD, line[1], Check_reg(line[2]), 0)
    elif line[0] == "DIV":
        return operator_node(operators.DIV, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "JMPT":
        return jmp_node(operators.JMPT, line[1], line[2])
    elif line[0] == "JMPF":
        return jmp_node(operators.JMPF, line[1], line[2])
    elif line[0] == "JMPE":
        return jmp_conditional_node(operators.JMPT, Check_reg(line[1]), Check_reg(line[2]), line[3])
    elif line[0] == "JMPNE":
        return jmp_conditional_node(operators.JMPF, Check_reg(line[1]), Check_reg(line[2]), line[3])
    elif line[0] == "LABEL":
        return label(line[1])
    elif line[0] == "JMPL":
        return jmp_label_node(operators.JMPL, line[1])
    elif line[0] == "PRT":
        return print_node(operators.PRINT, Check_reg(line[1]))
    else:
        return None

def execute(operation_node : node, Program_state : dict, program : [operator_node]) -> dict:
    if (isinstance(operation_node, operator_node)):
        return {operation_node.storage_register : operation_node.operator.value(Check_reg2(operation_node.parameter1, Program_state), Check_reg2(operation_node.parameter2, Program_state))}
    elif (isinstance(operation_node, jmp_node)):
        return operation_node.operator.value(Check_reg2(operation_node.condition, Program_state), operation_node.jmp_location)
    elif (isinstance(operation_node, jmp_conditional_node)):
        condition = Check_reg2(operation_node.parameter1, Program_state) == Check_reg2(operation_node.parameter2, Program_state)
        return operation_node.operator.value(condition, operation_node.jmp_location)
    elif (isinstance(operation_node, jmp_label_node)):
        return operation_node.operator.value(operation_node.name, program)
    elif (isinstance(operation_node, print_node)):
        operation_node.operator.value(Check_reg2(operation_node.value, Program_state))
        return {}
    else:      
        return {}

def run(Program_state : dict, program : [operator_node]) -> Program_state:
    New_Program_state = Program_state.copy()
    if len(program) <= 1:
        New_Program_state.update(execute(program[0], Program_state, program))
        return New_Program_state

    elif New_Program_state.get("PC") >= len(program):
        return New_Program_state

    else:        
        current_row_number = Program_state.get("PC")
        current_instruction = program[current_row_number]
        New_Program_state.update(execute(current_instruction, Program_state, program))
    New_Program_state.update({"PC": New_Program_state.get("PC") + 1})   
    return run(New_Program_state, program)

def Printing_read_file_into_lines(func: Callable) -> [str]:
    def inner(Filename):
        output = func(Filename)
        print("Lines: ")
        print(output)
        return output
    return inner

def Printing_lines_into_operations(func: Callable) -> [operator_node]:
    def inner(Lines: [str]):
        output = func(Lines)
        print("Nodes: ")
        list(map(print, output))
        return output
    return inner

def all_steps(Filename, Program_state : dict, Printing_state = "n") -> Program_state:
    global Read_file_into_lines
    global Lines_into_operations 

    if Printing_state == "y":
        Read_file_into_lines = Printing_read_file_into_lines(Read_file_into_lines)
        Lines_into_operations = Printing_lines_into_operations(Lines_into_operations)

    return run(Program_state, Lines_into_operations(Read_file_into_lines(Filename)))

output = all_steps("countermachine.txt", Program_state,"n")
print("Program_output: ", output)