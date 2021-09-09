import queue
case = 0
while True:
    case += 1
    s = []
    p, c = map(int, input().split())
    if p == 0:
        break
    q = queue.Queue()
    for i in range(1, min(p, c) + 1):
        q.put(i)
    print("Case {}:".format(case))
    for _ in range(c):
        line = input()
        if len(line) == 1:
            temp = q.get()
            q.put(temp)
            s.append(temp)
        else:
            x = int(line[2:])
            q.put(x)
            length = q.qsize()
            for i in range(length - 1):
                temp = q.get()
                if temp != x:
                    q.put(temp)
    for j in range(len(s)):
        print(s[j])