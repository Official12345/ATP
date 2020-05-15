from operators import *
from nodes import *
from typing import Callable, Union

Program_state = {"R0": 0, "R1": 0, "R2": 0, "R3": 0, "R4": 0, "R5": 0, "R6": 0, "R7": 0, "R8": 0, "R9": 0, "R10": 0, "R11": 0, "R12": 0, "R13": 0, "R14": 0, "PC": 0, }

#This is the decorator for the read_file_into_lines function
#It enables the function to print
def Printing_read_file_into_lines(func: Callable) -> Callable:
    def inner(Filename) -> [str]:
        output = func(Filename)
        print("Lines: ")
        list(map(print, output))
        return output
    return inner

#This is the decorator for the lines_into_operations function
#It enables the function to print
def Printing_lines_into_operations(func: Callable) -> Callable:
    def inner(Lines: [str]) -> [operator_node]:
        output = func(Lines)
        print("Nodes: ")
        list(map(print, output))
        return output
    return inner

#This function reads the programfile and returns a list of strings(one per line)
@Printing_read_file_into_lines
def Read_file_into_lines(filename) -> [str]:
    file = open(filename, "r")
    return file.read().splitlines()

#This funtion turns a list of strings into a list of operator_node
@Printing_lines_into_operations
def Lines_into_operations(Lines : [str]) -> [operator_node]:
    return list(map(Line_to_operation, Lines))

#This function turns a single line into a operator_node
def Line_to_operation(line : str) -> operator_node:
    line = line.split()
    if line[0] == "\n":
        return None
    elif line[0] == "IRONMAN":
        return operator_node(operators.ADD, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "THOR":
        return operator_node(operators.SUB, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "ANTMAN":
        return operator_node(operators.MUL, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "HULK":
        return operator_node(operators.DIV, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "DOCTORSTRANGE":
        return operator_node(operators.POW, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "DIEDERIK":
        return operator_node(operators.MOD, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "NICKFURY":
        return operator_node(operators.FDIV, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "KAECILIUS":
        return operator_node(operators.EQ, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "REDSKULL":
        return operator_node(operators.NEQ, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "ULTRON":
        return operator_node(operators.GRE, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "MANDARIN":
        return operator_node(operators.GREEQ, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "RONAN":
        return operator_node(operators.LES, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "MYSTERIO":
        return operator_node(operators.LESEQ, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "CAPTAINAMERICA":
        return operator_node(operators.ADD, line[1], Check_reg(line[2]), 0)
    elif line[0] == "BLACKWIDOW":
        return jmp_node(operators.JMPT, line[1], line[2])
    elif line[0] == "HAWKEYE":
        return jmp_node(operators.JMPF, line[1], line[2])
    elif line[0] == "SCARLETWITCH":
        return jmp_conditional_node(operators.JMPT, Check_reg(line[1]), Check_reg(line[2]), line[3])
    elif line[0] == "FALCON":
        return jmp_conditional_node(operators.JMPF, Check_reg(line[1]), Check_reg(line[2]), line[3])
    elif line[0] == "SPIDERMAN":
        return label(line[1])
    elif line[0] == "WARMACHINE":
        return jmp_label_node(operators.JMPL, line[1])
    elif line[0] == "VISION":
        return print_node(operators.PRINT, Check_reg(line[1]))
    else:
        return None

#This function checks if a string is a digit or not
def Check_reg(name : str) -> Union[str, int]:
    if(name.isdigit()):
        return int(name)
    elif (name[0] == '-' and name[1:].isdigit()):
        return int(name)
    else:
        return name

#This function checks if the variable already exists or not
#If it already exists, it returns its value       
def Check_existing(name : str, Program_state : dict) -> int:
    if(type(name) == int):
        return name
    else:
        return Program_state.get(name)

#This function executes a node by calling its operator
def execute(operation_node : node, Program_state : dict, program : [operator_node]) -> dict:
    if (isinstance(operation_node, operator_node)):
        return {operation_node.storage_register : operation_node.operator.value(Check_existing(operation_node.parameter1, Program_state), Check_existing(operation_node.parameter2, Program_state))}
    elif (isinstance(operation_node, jmp_node)):
        return operation_node.operator.value(Check_existing(operation_node.condition, Program_state), operation_node.jmp_location)
    elif (isinstance(operation_node, jmp_conditional_node)):
        condition = Check_existing(operation_node.parameter1, Program_state) == Check_existing(operation_node.parameter2, Program_state)
        return operation_node.operator.value(condition, operation_node.jmp_location)
    elif (isinstance(operation_node, jmp_label_node)):
        return operation_node.operator.value(operation_node.name, program)
    elif (isinstance(operation_node, print_node)):
        operation_node.operator.value(Check_existing(operation_node.value, Program_state))
        return {}
    else:      
        return {}

#This function executes a complete program(list of nodes)
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



#This is the main function
#It contains the lexing, parsing and execution steps
def all_steps(Filename, Program_state : dict, Printing_state = 0) -> Program_state:

    return run(Program_state, Lines_into_operations(Read_file_into_lines(Filename)))

output = all_steps("countermachine.txt", Program_state, 1)
print("Program_output: ", output)