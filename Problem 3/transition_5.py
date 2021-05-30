from sympy import *
from transition_4 import get_N, parse_frac

P = get_N()

t = P * ones(19, 1)

f = open("transition3_5.tex", "w")

f.write(r"$$")
f.write("\n")
f.write(r"\bm{t} = ")
f.write("\n")

f.write(r"\left ( \scalemath{0.55} { \begin{array}{c}")
f.write("\n")

for i in range(19):
    s = ""
    s += parse_frac(t[i])
    s += r"\\"
    s += "\n"
    f.write(s)


f.write(r"\end{array} } \right)")

f.write("\n")
f.write(r"$$")
f.write("\n")

f.close()
