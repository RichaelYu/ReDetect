from z3 import *

x = BitVec("x", 256)
solver = Solver()
solver.add(x == x +1)
print(solver.check())