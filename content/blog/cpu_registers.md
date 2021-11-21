
Four kinds of Registers.

1. General Purpose Registers
2. Segment Registers
3. Program Status and Control Register
4. Instruction Pointer Register

1. General Purpose Register: These registers are used as operand for operations
like logical and arithmetic operation, and memory pointer. In a 32 bit
(386-based processor or later) system there are eight general purpose registers
(each 32 bits long).
However, in 64 bit systems (amd64), there are 16 general purpose registers.

	* `EAX`, `EBX`, `ECX`, `EDX` -
	* `ESI`, `EDI` -
	* `EBP` - pointer to memory buffer for the function (contains local variable with function scope)
	* `ESP` - pointer to current stack location

4. Instruction Pointer register contains the memory address for the next instruction to be executed. This register cannot be accessed directly by software and it is controlled implicitly by control transfer instructions like `JMP`, `JCC`, `CALL` and `RET`. In 32 bit mode, instruction pointer is `EIP` which is 32 bits long and in 64 bit mode, instruction pointer is 64 bits long and named as `RIP`.
