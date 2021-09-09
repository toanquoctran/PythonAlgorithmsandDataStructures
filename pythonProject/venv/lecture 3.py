n = int(input())
l = list(map(int, input().split()))
l.sort()
max = 1
count = 1
for i in range(n-1):
    if l[i+1] == l[i]:
        count += 1
        n -= 1
        if max < count:
            max = count
    else:
        count = 1
print(max, n)