import queue

def bfs(s, t):
    visited = [False for _ in range(999999)]
    dist = [-1 for _ in range(999999)]
    if s == t:
        return -1
    q = queue.Queue()
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                dist[v] = dist[u] + 1
    return dist[t]

if __name__ == "__main__":
    n = int(input())
    input()
    for _ in range(n):
        dict = []
        graph = [[] for _ in range(999999)]
        while True:
            availableWords = input()
            dict.append(availableWords)
            if availableWords == "*":
                break
        for i in range(len(dict)):
            for j in range(i + 1, len(dict)):
                if len(dict[j]) == len(dict[i]):
                    count = 0
                    for k in range(len(dict[i])):
                        if dict[j][k] != dict[i][k]:
                            count += 1
                    if count == 1:
                        graph[i].append(j)
                        graph[j].append(i)
        while True:
            try:
                pairs = input().split()
            except EOFError:
                break
            if len(pairs) == 0:
                break
            s = dict.index(pairs[0])
            t = dict.index(pairs[1])
            res = bfs(s, t)
            print(pairs[0], pairs[1], res + 1)