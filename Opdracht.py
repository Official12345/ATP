from enum import Enum

Program_state = {"R0": 0, "R1": 0, "R2": 0, "R3": 0, "R4": 0, "R5": 0, "R6": 0, "R7": 0, "R8": 0, "R9": 0, "R10": 0, "R11": 0, "R12": 0, "R13": 0, "R14": 0, "R15": 0, }

class operators(Enum):
    ADD = lambda a, b : a + b
    SUB = lambda a, b : a - b


class operator_node:
    def __init__(self, operator, storage_register, parameter1, parameter2):
        self.operator = operator
        self.storage_register = storage_register
        self.parameter1 = parameter1
        self.parameter2 = parameter2

def Read_file_into_lines(filename) -> [[str]]:
    file = open(filename, "r")
    return file.read().splitlines()

def Lines_into_operations(Lines : [[str]]) -> [operator_node]:
    return 

def Check_reg(name : str):# -> Union[int, str]:
    #print('name ',name)
    if(name.isdigit()):
        return int(name)
    else:
        #print(name, Program_state.get(name))
        return name
        
def Check_reg2(name : str, Program_state):# -> Union[int, str]:
    #print('name ',name)
    if(type(name) == int):
        return name
    else:
        return Program_state.get(name)

def Line_to_operation(line : [str]) -> operator_node:
    line = line.split()
    if line[0] == "ADD":
        #return operator_node(operators.ADD, line[1], int(line[2]), int(line[3]))
        #print(line[2])
        #print("program state: ", Program_state)
        # return operator_node(operators.ADD, line[1], Check_reg(line[2], Program_state), Check_reg(line[3], Program_state))
        return operator_node(operators.ADD, line[1], Check_reg(line[2]), Check_reg(line[3]))
    elif line[0] == "SUB":
        return operator_node(operators.SUB, line[1], Check_reg(line[2]), Check_reg(line[3]))
    else:
        return None

def execute(operation_node, Program_state) -> dict:
    # New_program_state = Program_state.update({operation_node.storage_register : operation_node.operator(operation_node.parameter1, operation_node.parameter2)})
    # return New_program_state
    # print("operation_node storage_register type: value: ", type(operation_node.storage_register), operation_node.storage_register)
    # print("operation_node parameter1 type: value: ", type(operation_node.parameter1), operation_node.parameter1)
    # print("operation_node parameter2 type: value: ", type(operation_node.parameter2), operation_node.parameter2, "\n")

    return {operation_node.storage_register : operation_node.operator(Check_reg2(operation_node.parameter1, Program_state), Check_reg2(operation_node.parameter2, Program_state))}

def run(Program_state : dict, program : list) -> Program_state:
    #print("Program_state: ", Program_state)
    if len(program) <= 1:
        Program_state.update(execute(program[0], Program_state))
        return Program_state
    else:
        head, *tail = program
        #head.execute()
        Program_state.update(execute(head, Program_state))
        # print("Program_ state end: ", Program_state)
    return run(Program_state, tail)


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

programlines = Read_file_into_lines("code.txt")

program = []

# program.append(Line_to_operation(programlines[0]))
# program.append(Line_to_operation(programlines[1]))
# program.append(Line_to_operation(programlines[2]))
# program.append(Line_to_operation(programlines[3]))
# program.append(Line_to_operation(programlines[4]))

for i in range(len(programlines)):
    program.append(Line_to_operation(programlines[i]))

output = run(Program_state, program)
print("Program_output: ", output)
#print(Program_state)
#print("end ", Program_state.get("R5"))