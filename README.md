# AVENGERS ASSEMBLER!
AVENGERS ASSEMBLER! is a programming themed after the avengers MCU and cortex-m0 assembler.<br>
Like they say in dutch "Een beetje van jezelf en een beetje van maggi.".

## Should-haves
### Creating your own language
My language differs from cortex-m0 assembler in too many ways to not be called a new language. <br>
You can declare your own variables. You also have more comparison operators than normal cortex-m0 assembler offers, And last but not least the amazing syntax this language uses ofcourse.

### Advanced language features
This language offers many operators that makes using it more flexable than using just a barebones turing-complete language. This includes multiple ways to jump in the program, aswell as most comparison operators you would want to use in any programmingl language.

## Variables
Like assembler, this language has 16 base registers, the 16th(R15) being used for the Program Counter.<br>
But unlike traditional assembler, AVENGERS ASSEMBLER! gives you the ability to declare your own variables. You can simply do this by using IRONMAN, THOR, ANTMAN, HULK OR CAPTAINAMERICA use a new name as the storage variable.

## List of instructions

| Name              | Instruction       | Example               | Explanation
| -------------     |:--------          |:------------          |:--------|
| IRONMAN           | ADDITION          | IRONMAN S P1 P2       | Add P1 and P2 and store it in S
| THOR              | SUBTRACTION       | THOR S P1 P2          | Subtract P2 from P1 and store it in S
| ANTMAN            | MULTIPLICATION    | ANTMAN S P1 P2        | Multiply P1 and P2 and store it in S
| HULK              | DIVISION          | HULK S P1 P2          | Divide P1 by P2 and store it in S
| DOCTORSTRANGE     | POWER             | DOCTORSTRANGE S P1 P2 | Raise P1 to the power of P2 and store it in S
| DIEDERIK          | MODULUS           | DIEDERIK S P1 P2      | Divide P1 by P2 and store the remainder in S
| NICKFURY          | FLOOR DIVISION    | NICKFURY S P1 P2      | Divide P1 by P2 and the value before the point in S
| KAECILIUS         | EQUALS            | KAECILIUS S P1 P2     | Store P1 == P2 in S
| REDSKULL          | NOT EQUALS        | REDSKULL S P1 P2      | Store P1 != P2 in S
| ULTRON            | GREATER           | ULTRON S P1 P2        | Store P1 > P2 in S
| MANDARIN          | EQUALS OR EQUALS  | MANDARIN S P1 P2      | Store P1 >= P2 in S
| RONAN             | LESSER            | RONAN S P1 P2         | Store P1 < P2 in S
| MYSTERIO          | LESSER OR EQUALS  | MYSTERIO S P1 P2      | Store P1 <= P2 in S
| CAPTAINAMERICA    | STORE             | CAPTAINAMERICA S P1   | Stores P1 in S
| BLACKWIDOW        | JUMP TRUE         | BLACKWIDOW P1 R       | If P1 is true, jump to row rumber R
| HAWKEYE           | JUMP FALSE        | HAWKEYE P1 R          | If P1 is false, jump to row rumber R
| VISION            | PRINT             | VISION P1             | Print P1
| SCARLETWITCH      | JUMP EQUAL        | SCARLETWITCH P1 P2 R  | If P1 equals P2, jump to row rumber R
| FALCON            | JUMP NOT EQUAL    | FALCON P1 P2 R        | If P1 does not equal P2, jump to row rumber R |
| SPIDERMAN         | MAKE LABEL        | SPIDERMAN NAME        | Makes a label called NAME
| WARMACHINE        | JUMP LABEL        | WARMACHINE NAME       | Jump to a label called NAME

###### My favorite is the modulus operator :P

## Example
Here is an example of the minsky countermachine: <br>
```
CAPTAINAMERICA R1 0
IRONMAN R1 R1 1
THOR R1 R1 1
CAPTAINAMERICA R2 R1
HAWKEYE R1 7
CAPTAINAMERICA R3 10
SCARLETWITCH R1 R2 9
CAPTAINAMERICA R4 10
CAPTAINAMERICA R5 10
```

## How to run
All you have to do to run your code is: 

```
output = all_steps("countermachine.txt", Program_state, 1)
print("Program_output: ", output)
```

Here you can change the textfile you want to run, in this case it is countermachine.txt. The last variable is whether you want printing mode turned on or off.<br>

Printing mode prints the raw output of the lexing and parsing steps, aswell as the regular output.<br>

The output of the code above is as follows with printing mode off:

```
Program_output:  {'R0': 0, 'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0, 'R5': 10, 'R6': 0, 'R7': 0, 'R8': 0, 'R9': 0, 'R10': 0, 'R11': 0, 'R12': 0, 'R13': 0, 'R14': 0, 'PC': 9}
```

And with printing mode turned on:

```
Lines: 
['CAPTAINAMERICA R1 0', 'IRONMAN R1 R1 1', 'THOR R1 R1 1', 'CAPTAINAMERICA R2 R1', 'HAWKEYE R1 7', 'CAPTAINAMERICA R3 10', 'SCARLETWITCH R1 R2 9', 'CAPTAINAMERICA R4 10', 'CAPTAINAMERICA R5 10']
Nodes: 
<class 'nodes.operator_node'> Operator: ADDITION Storage_register: R1 Parameter1: 0 Parameter2: 0
<class 'nodes.operator_node'> Operator: ADDITION Storage_register: R1 Parameter1: R1 Parameter2: 1
<class 'nodes.operator_node'> Operator: SUBTRACT Storage_register: R1 Parameter1: R1 Parameter2: 1
<class 'nodes.operator_node'> Operator: ADDITION Storage_register: R2 Parameter1: R1 Parameter2: 0
<class 'nodes.jmp_node'> Operator: JUMP_FALSE Condition: R1 jmp_location: 7
<class 'nodes.operator_node'> Operator: ADDITION Storage_register: R3 Parameter1: 10 Parameter2: 0
<class 'nodes.jmp_conditional_node'> Operator: JUMP_TRUE Jmp_location: 9 Parameter1: R1 Parameter2: R2
<class 'nodes.operator_node'> Operator: ADDITION Storage_register: R4 Parameter1: 10 Parameter2: 0
<class 'nodes.operator_node'> Operator: ADDITION Storage_register: R5 Parameter1: 10 Parameter2: 0
Program_output:  {'R0': 0, 'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0, 'R5': 10, 'R6': 0, 'R7': 0, 'R8': 0, 'R9': 0, 'R10': 0, 'R11': 0, 'R12': 0, 'R13': 0, 'R14': 0, 'PC': 9}
```










