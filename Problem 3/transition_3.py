from transition import func

def func_2(a, b):
    if(a == b):
        return 1-func(a, b)
    else:
        return func(a, b)


f = open("transition3_3.tex", "w")

f.write(r"$$")
f.write("\n")
f.write(r"N^{-1} = ")
f.write("\n")

f.write(r"\left ( \scalemath{0.35} { \begin{array}{cccccccccccccccccccc}")
f.write("\n")

for i in range(20):
    s = "\t"
    for j in range(20):
        s += "p_{{ {}, {} }} = ".format(i, j)
        s += str(func_2(i, j))
        s += " & "
    s = s[:-3]
    f.write(s)
    f.write(r"\\")
    f.write("\n")

f.write(r"\end{array} } \right)")

f.write("\n")
f.write(r"$$")
f.write("\n")

f.close()
