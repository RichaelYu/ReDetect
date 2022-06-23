# Code Structure

### *oyente.py*

This is the main entry point to the program. Oyente is able to analyze smart contracts via the following inputs
- solidity program
- evm bytecode


Other configuration options include getting the input state, setting timeouts for z3, etc. (Check ```python oyente.py --help``` or ```global_params.py```  for the full list of configuration options available).
These options are collated and set in the *global_params* module which will be used during the rest of the execution.

The contracts are then disassembled into opcodes using the ```evm disasm``` command.

After this, the symexec module is called with the disassembled file which carries out the analyses of the contracts for various vulnerabilities (TOD, timestamp-dependence, mishandled exceptions).

### *symExec.py*

The analysis starts off with the ```build_cfg_and_analyze``` function. We break up the disasm file created by oyente.py into tokens using the native tokenize python module.

The *collect_vertices* and *construct_bb* functions identify the basic blocks in the program and we store them as vertices. Basic blocks are identified by using opcodes like ```JUMPDEST```, ```STOP```, ```RETURN```, ```SUICIDE```, ```JUMP``` and ```JUMPI``` as separators. Each basic block is backed by an instance of BasicBlock class defined in basicblock.py

After the basic blocks are created, we start to symbolically execute each basic block with the full_sym_exec function. We get the instructions stored in each basic block and execute each of them symbolically via the sym_exec_ins function. In this function, we model each opcode as closely as possible to the behaviour described in the ethereum yellow paper. Some interesting details regarding each class of opcodes is discussed below.

#### Model
The stack is modelled using a simple python list.
The memory is modelled as a growing list. The maximum index of used by the memory list is stored as ```current_miu_i``` variable.
The storage is stored as a python object as key-value pairs.

