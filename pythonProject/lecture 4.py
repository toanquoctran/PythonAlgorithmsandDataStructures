import queue
c = int(input())
class Car:
    def __init__(self, id, time):
        self.id = id
        self.time = time
def process(Side, curTime, N, T):
    count = 0
    while not Side.empty() and Side.queue[0].time <= curTime and count < N:
        car = Side.get()
        arriveTime[car.id] = curTime + T
        count += 1
for _ in range(c):
    n, T, m = map(int, input().split())
    leftSide = queue.Queue()
    rightSide = queue.Queue()
    curTime = 0
    curSide = 0
    nextTime = 0
    arriveTime = [0]*m
    for i in range(m):
        time, side = input().split()
        time = int(time)
        if side == "left":
            leftSide.put(Car(i, time))
        else:
            rightSide.put(Car(i, time))
    while leftSide.qsize() != 0 or rightSide.qsize() != 0:
        if leftSide.qsize() == 0:
            nextTime = rightSide.queue[0].time
        elif rightSide.qsize() == 0:
            nextTime = leftSide.queue[0].time
        else:
            nextTime = min(rightSide.queue[0].time, leftSide.queue[0].time)
        curTime = max(curTime, nextTime)
        if curSide == 0:
            process(leftSide, curTime, n, T)
        else:
            process(rightSide, curTime, n, T)
    for i in range(m):
        print(arriveTime[i])
    print()