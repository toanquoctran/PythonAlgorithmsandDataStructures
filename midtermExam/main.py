import queue

class PQEntry:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        pq = queue.PriorityQueue()
        q = queue.Queue()
        n, m = map(int, input().split())
        priorities = list(map(int, input().split()))
        for i in range(len(priorities)):
            pq.put(PQEntry(priorities[i]))
            q.put((i, priorities[i]))
        time = 0
        while True:
            index, job = q.get()
            rank = pq.get()
            if rank.value == job:
                time += 1
                if index == m:
                    break
            else:
                q.put((index, job))
                pq.put(rank)
        print(time)