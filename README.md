# AVENGERS ASSEMBLER!
AVENGERS ASSEMBLER! is a programming themed after the avengers MCU and cortex-m0 assembler.<br>
Like they say in dutch "Een beetje van jezelf en een beetje van maggi.".

## Variables
Like assembler, this language has 16 base registers, the 16th(R15) being used for the Program Counter.<br>
But unlike traditional assembler, AVENGERS ASSEMBLER! gives you the ability to declare your own variables.

## List of instructions

| Name            | Instruction              | Example  | Explanation
| ------------- |:-------------:| ------------:|--------:|
| IRONMAN           | ADDITION          | IRONMAN S P1 P2 | Add P1 and P2 and store it in S
| THOR              | SUBTRACTION       | THOR S P1 P2 | Subtract P2 from P1 and store it in S
| ANTMAN            | MULTIPLICATION    | ANTMAN S P1 P2 | Multiply P1 and P2 and store it in S
| HULK              | DIVISION          | HULK S P1 P2 | Divide P1 by P2 and store it in S
| CAPTAINAMERICA    | STORE             | CAPTAINAMERICA S P1 | Stores P1 in S
| BLACKWIDOW        | JUMP TRUE         | BLACKWIDOW P1 R | If P1 is true, jump to row rumber R
| HAWKEYE           | JUMP FALSE        | HAWKEYE P1 R | If P1 is false, jump to row rumber R
| VISION            | PRINT             | VISION P1 | Print P1
| SCARLETWITCH      | JUMP EQUAL        | SCARLETWITCH P1 P2 R | If P1 equals P2, jump to row rumber R
| FALCON            | JUMP NOT EQUAL    | FALCON P1 P2 R | If P1 does not equal P2, jump to row rumber R |
| SPIDERMAN         | MAKE LABEL        | SPIDERMAN NAME | Makes a label called NAME
| WARMACHINE        | JUMP LABEL        | WARMACHINE NAME | Jump to a label called NAME
