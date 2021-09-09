needTree = array = automaton = False
a = []
b = []
s = input()
t = input()
for c in s:
    a.append(c)

for d in t:
    b.append(d)

if len(a) < len(b):
    needTree = True
if len(a) == len(b):
    if set(b).issubset(a):
        needTree = False
    else:
        needTree = True
if len(a) > len(b):
    if set(b).issubset(a):
        automaton = True
    else:
        needTree = True
temp = 0
for i in range(len(t)):
    index = s.find(t[i], temp)
    if index >= i:
        temp = index
    else:
        array = True
        break
if needTree:
    print('need tree')
else:
    if automaton:
        if not array:
            print('automaton')
        else:
            print('both')
    else:
        print('array')