n = int(input())
t = list(map(int, input().split()))
d = 1
a = 0
b = 0
l = 0
for i in range(1, n):
    temp = t[i] - t[i - 1]
    if temp != 0:
        if temp == a:
            l = b + 1
        b = i - 1
        a = temp
    d = max(d, i - l + 1)
print(d)