if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    i = int(n/2)
    print(a[i])