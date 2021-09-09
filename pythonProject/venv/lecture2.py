n, k = map(int, input().split())
l = list(map(int, input().split()))
a = {}
j = 0
for i in l:
    j += 1
    a[i] = j
    if len(a) == k:
        print(min(a.values()), max(a.values()))
        quit()
print('-1 -1')