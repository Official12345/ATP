class node:
    pass

class operator_node(node):
    def __init__(self, operator, storage_register, parameter1, parameter2):
        self.operator = operator
        self.storage_register = storage_register
        self.parameter1 = parameter1
        self.parameter2 = parameter2

    def __str__(self):
        return '{} Operator: {} Storage_register: {} Parameter1: {} Parameter2: {}'.format(type(self), self.operator.__name__, self.storage_register, self.parameter1, self.parameter2)

    def __repr(self):
        return self.__str__()

class jmp_node(node):
    def __init__(self, operator, condition, jmp_location):
        self.operator = operator
        self.condition = condition
        self.jmp_location = jmp_location

    def __str__(self):
        return '{} Operator: {} Condition: {} jmp_location: {}'.format(type(self), self.operator.__name__, self.condition, self.jmp_location)

    def __repr(self):
        return self.__str__()

class jmp_conditional_node(node):
    def __init__(self, operator, parameter1, parameter2, jmp_location):
        self.operator = operator
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.jmp_location = jmp_location   

    def __str__(self):
        return '{} Operator: {} Jmp_location: {} Parameter1: {} Parameter2: {}'.format(type(self), self.operator.__name__, self.jmp_location, self.parameter1, self.parameter2)

    def __repr(self):
        return self.__str__()

class jmp_label_node(node):
    def __init__(self, operator, name):
        self.operator = operator
        self.name = name

    def __str__(self):
        return '{} Operator: {} Name: {}'.format(type(self), self.operator.__name__, self.name)

    def __repr(self):
        return self.__str__()

class label(node):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} Name: {}'.format(type(self), self.name)

    def __repr(self):
        return self.__str__()