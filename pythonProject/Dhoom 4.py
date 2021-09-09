import queue
s, b = map(int, input().split())
n = int(input())
v = list(map(int, input().split()))
visited = [False for i in range(100001)]
dist = [-1 for _ in range(100001)]
a = []
q = queue.Queue()
def bfs(s, b):
    visited[s] = True
    q.put(s)
    dist[s] = 0
    while not q.empty():
        s = q.get()
        if s == b:
            break
        for i in range(n):
            temp = s * a[i]
            temp %= 100000
            if not visited[temp]:
                visited[temp] = True
                dist[temp] = dist[s] + 1
                q.put(temp)
    return dist[b]
if __name__ == "__main__":
    res = bfs(s, b)
    print(res)