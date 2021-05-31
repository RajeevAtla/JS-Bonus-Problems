from sympy import eye, Rational, simplify, zeros
from transition import func


def get_N():
    P = zeros(19, 19)
    for i in range(19):
        for j in range(19):
            if func(i, j) == r"\frac{1}{6}":
                P[i, j] = Rational(1, 6)
            elif func(i, j) == r"\frac{1}{2}":
                P[i, j] = Rational(1, 2)
            elif func(i, j) == r"\frac{1}{3}":
                P[i, j] = Rational(1, 3)
            else:
                P[i, j] = func(i, j)
    P = eye(19) - P
    P = P.inv(method="LDL")
    return P


def parse_frac(f):
    f = simplify(f)
    arr = str(f).split("/")
    s = r"\frac{" + arr[0] + r"}{" + arr[1] + r"}"
    return s


P = get_N()

f = open("transition3_4.tex", "w")

f.write(r"$$")
f.write("\n")
f.write("N = ")
f.write("\n")

f.write(r"\left ( \scalemath{0.3} { \begin{array}{ccccccccccccccccccc}")
f.write("\n")

for i in range(19):
    s = "\t"
    for j in range(19):
        s += "p_{{ {}, {} }} = ".format(i, j)
        s += parse_frac(P[i, j])
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
