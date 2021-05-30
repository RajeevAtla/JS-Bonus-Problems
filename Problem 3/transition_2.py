from transition import func

f = open('transition3_2.tex', 'w')

f.write(r'$$')
f.write('\n')
f.write('Q = ')
f.write('\n')

f.write(r'\left ( \scalemath{0.4} { \begin{array}{ccccccccccccccccccc}')
f.write('\n')

for i in range(19):
    s = '\t'
    for j in range(19):
        s += 'p_{{ {}, {} }} = '.format(i, j)
        s += str(func(i, j))
        s += ' & '
    s = s[:-3]
    f.write(s)
    f.write(r'\\')
    f.write('\n')

f.write(r'\end{array} } \right)')

f.write('\n')
f.write(r'$$')
f.write('\n')

f.close()