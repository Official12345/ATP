from operators import *
from nodes import *

Program_state = {"R0": 0, "R1": 0, "R2": 0, "R3": 0, "R4": 0, "R5": 0, "R6": 0, "R7": 0, "R8": 0, "R9": 0, "R10": 0, "R11": 0, "R12": 0, "R13": 0, "R14": 0, "R15": 0, }

def Read_file_into_lines(filename) -> [str]:
    file = open(filename, "r")
    return file.read().splitlines()

def Lines_into_operations(Lines : [str]) -> [operator_node]:
    return list(map(Line_to_operation, Lines))

def Check_reg(name : str):# -> Union[int, str]:
    #print('name ',name)
    if(name.isdigit()):
        return int(name)
    elif (name[0] == '-' and name[1:].isdigit()):
        return int(name)

    else:
        #print(name, Program_state.get(name))
        return name
        
def Check_reg2(name : str, Program_state : dict):# -> Union[int, str]:
    #print('name ',name)
    if(type(name) == int):
        return name
    else:
        return Program_state.get(name)

def Line_to_operation(line : str) -> operator_node:
    line = line.split()
    if line[0] == "\n":
        return None
    elif line[0] == "ADD":
        #return operator_node(operators.ADD, line[1], int(line[2]), int(line[3]))
        #print(line[2])
        #print("program state: ", Program_state)
        # return operator_node(operators.ADD, line[1], Check_reg(line[2], Program_state), Check_reg(line[3], Program_state))
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
        return jmp_label_node(jump_label, line[1])
    else:
        return None

def execute(operation_node : node, Program_state : dict, program : [operator_node]) -> dict:
    # New_program_state = Program_state.update({operation_node.storage_register : operation_node.operator(operation_node.parameter1, operation_node.parameter2)})
    # return New_program_state
    # print("operation_node storage_register type: value: ", type(operation_node.storage_register), operation_node.storage_register)
    # print("operation_node parameter1 type: value: ", type(operation_node.parameter1), operation_node.parameter1)
    # print("operation_node parameter2 type: value: ", type(operation_node.parameter2), operation_node.parameter2, "\n")
    # print(type(operation_node) == operator_node)
    # print(type(operation_node) == jmp_node)
    if (isinstance(operation_node, operator_node)):
        return {operation_node.storage_register : operation_node.operator(Check_reg2(operation_node.parameter1, Program_state), Check_reg2(operation_node.parameter2, Program_state))}
    elif (isinstance(operation_node, jmp_node)):
        return operation_node.operator(Check_reg2(operation_node.condition, Program_state), operation_node.jmp_location)
    elif (isinstance(operation_node, jmp_conditional_node)):
        condition = Check_reg2(operation_node.parameter1, Program_state) == Check_reg2(operation_node.parameter2, Program_state)
        return operation_node.operator(condition, operation_node.jmp_location)
    elif (isinstance(operation_node, jmp_label_node)):
        # return jump_label(operation_node.name, program)
        return operation_node.operator(operation_node.name, program)
    else:      
        return {}

# def run(Program_state : dict, program : list) -> Program_state:
#     #print("Program_state: ", Program_state)
#     if len(program) <= 1:
#         Program_state.update(execute(program[0], Program_state))
#         return Program_state
#     else:
#         head, *tail = program
#         New_Program_state = Program_state.copy()
#         New_Program_state.update(execute(head, Program_state))
#         # print("Program_ state end: ", Program_state)
#         #Program_state.update({"R15": Program_state.get("R15") + 1})
#         New_Program_state.update({"R15": Program_state.get("R15") + 1})
#     return run(New_Program_state, tail)

def run(Program_state : dict, program : [operator_node]) -> Program_state:
    New_Program_state = Program_state.copy()
    print("row_number ", New_Program_state.get("R15"))
    if len(program) <= 1:
        New_Program_state.update(execute(program[0], Program_state, program))
        return New_Program_state

    elif New_Program_state.get("R15") >= len(program):
        return New_Program_state

    else:        
        current_row_number = Program_state.get("R15")
        #print("row_number ", current_row_number)
        current_instruction = program[current_row_number]
        New_Program_state.update(execute(current_instruction, Program_state, program))
        # print("Program_ state end: ", Program_state)
        #Program_state.update({"R15": Program_state.get("R15") + 1})
    New_Program_state.update({"R15": New_Program_state.get("R15") + 1})   
    return run(New_Program_state, program)


#print(Read_file_into_lines("code.txt"))

# program = Read_file_into_lines("code.txt")
# operations = []
# operations.append(Line_to_operation((program[0]), Program_state))
# operations[0].execute() 
# operations.append(Line_to_operation((program[1]), Program_state))
# operations[1].execute() 
# operations.append(Line_to_operation((program[2]), Program_state))
# operations[2].execute() 
# operations.append(Line_to_operation((program[3]), Program_state))
# operations[3].execute()   

# for operation in operations:
#     operation.execute()

# program.append(Line_to_operation(programlines[0]))
# program.append(Line_to_operation(programlines[1]))
# program.append(Line_to_operation(programlines[2]))
# program.append(Line_to_operation(programlines[3]))
# program.append(Line_to_operation(programlines[4]))

#programlines = Read_file_into_lines("code.txt")
#Lines_into_operations(Read_file_into_lines("code.txt"))
# program = []

# for i in range(len(programlines)):
#     program.append(Line_to_operation(programlines[i]))

# output = run(Program_state, program)
# print("Program_output: ", output)

#def all_steps(Program_state : dict) -> Program_state:


output = run(Program_state, Lines_into_operations(Read_file_into_lines("code.txt")))
print("Program_output: ", output)

a = node()
b = operator_node(1, 2, 3, 4)
c = jmp_node(1, 2, 3)
d = jmp_conditional_node(1, 2, 3, 4)
e = jmp_label_node(1, 2)
f = label(1)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)



#print(Program_state)
#print("end ", Program_state.get("R5"))