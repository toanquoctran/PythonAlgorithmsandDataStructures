n = int(input())
a = list(map(int, input().split()))
ranking = [0] * 2001
b = sorted(a, reverse = True)
count = 0
ranking[b[0]] = 1
for i in range(1, len(b)):
    if b[i] == b[i-1]:
        ranking[b[i]] = ranking[b[i-1]]
        count += 1
    else:
        ranking[b[i]] = ranking[b[i-1]] + 1 + count
        count = 0
for i in range(len(a)):
    print(ranking[a[i]], end = " ")