def func(a, b):
    # a is state 1
    # b is state 2
    # this is horrible code but it works! :^)
    s = r"\frac{1}{6}"
    s1 = r"\frac{1}{2}"
    s2 = r"\frac{1}{3}"
    if a == 19 and b != 19:
        return 0
    if a == b:
        if a == 19:
            return 1
        else:
            return 0
    elif a == 0:
        if b <= 6:
            return s
        else:
            return 0
    elif a <= 6:
        if b == 0:
            return s
        elif b > 18:
            return 0
        else:
            if a == 1 and (b in [2, 6, 7, 8, 9]):
                return s
            elif a == 2 and (b in [1, 3, 9, 10, 11]):
                return s
            elif a == 3 and (b in [2, 4, 11, 12, 13]):
                return s
            elif a == 4 and (b in [3, 5, 13, 14, 15]):
                return s
            elif a == 5 and (b in [4, 6, 15, 16, 17]):
                return s
            elif a == 6 and (b in [1, 5, 7, 17, 18]):
                return s
            else:
                return 0
    else:
        if b == 19:
            if a % 2 == 1:
                return s2
            else:
                return s1
        else:
            if b == 0:
                return 0
            elif b in [a - 1, a + 1]:
                return s
            elif a == 7 and b == 18:
                return s
            elif b == 7 and a == 18:
                return s
            else:
                if a % 2 == 1:
                    arr = list(map(int, [0.5 * a - 3.5, 0.5 * a - 2.5]))
                    if b in arr:
                        return s
                    else:
                        return 0
                else:
                    if b == int(0.5 * a - 3):
                        return s
                    else:
                        return 0


f = open("transition3.tex", "w")

f.write(r"$$")
f.write("\n")
f.write("P = ")
f.write("\n")

f.write(r"\left ( \scalemath{0.4} { \begin{array}{cccccccccccccccccccc}")
f.write("\n")

for i in range(20):
    s = "\t"
    for j in range(20):
        s += "p_{{ {}, {} }} = ".format(i, j)
        s += str(func(i, j))
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
