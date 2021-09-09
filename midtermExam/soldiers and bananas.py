if __name__ == "__main__":
    k, n, w = map(int, input().split())
    sumI = 0
    for i in range(w):
        sumI += i + 1
    borrow = sumI * k - n
    if borrow <= 0:
        print(0)
    else:
        print(borrow)