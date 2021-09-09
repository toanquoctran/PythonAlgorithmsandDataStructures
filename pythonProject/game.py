needTree = array = automaton = False
a = []
b = []
s = input()
t = input()
for c in s:
    a.append(c)
a.sort()
for d in t:
    b.append(d)
b.sort()
if len(a) < len(b):
    needTree = True
if len(a) == len(b):
    if all(item in b for item in a)
        needTree = False
    else:
        needTree = True
if len(a) > len(b):
    if all(item in b for item in a)
        automation = True
    else:
        needTree = True
temp = 0
for i in range(b):
    index = a.find(b[i], temp, len(b))
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