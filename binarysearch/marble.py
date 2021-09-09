def bsFirst(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == left or x > a[mid - 1]) and a[mid] == x:
            return mid
        elif x > a[mid]:
            return bsFirst(a, mid + 1, right, x)
        else:
            return bsFirst(a, left, mid - 1, x)
    return -1

if __name__ == "__main__":
    case = 1
    while True:
        n, q = map(int, input().split())
        if n == 0 and q == 0:
            break
        marbles = []
        
        for _ in range(n):
            marbles.append(int(input()))
        marbles.sort()
        
        print("CASE# {}:".format(case))
        case += 1
        
        for _ in range(q):
            number = int(input())
            if bsFirst(marbles, 0, n - 1, number) == -1:
                print("{} not found".format(number))
            else:
                print("{} found at {}".format(number, bsFirst(marbles, 0, n - 1, number) + 1))