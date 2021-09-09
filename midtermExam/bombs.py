import queue

def bfs(rowS, colS, rowD, colD):
    visited[rowS][colS] = True
    q = queue.Queue()
    q.put((rowS, colS))
    while not q.empty():
        curRow, curCol = q.get()
        for i in range(4):
            newRow = curRow + dx[i]
            newCol = curCol + dy[i]
            if 0 <= newRow < r and 0 <= newCol < c and maze[newRow][newCol] == 0 and not visited[newRow][newCol]:
                visited[newRow][newCol] = True
                dist[newRow][newCol] = dist[curRow][curCol] + 1
                q.put((newRow, newCol))
                if newRow == rowD and newCol == colD:
                    break
    return dist[rowD][colD]

if __name__ == "__main__":
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while True:
        r, c = map(int, input().split())
        dist = [[-1 for _ in range(c)] for _ in range(r)]
        visited = [[False for _ in range(c)] for _ in range(r)]
        if r == 0 and c == 0:
            break
        rows = int(input())
        maze = [[0 for _ in range(c)] for _ in range(r)]
        for _ in range(rows):
            locations = list(map(int, input().split()))
            for i in range(locations[1]):
                maze[locations[0]][locations[i + 2]] = 1
        rowS, colS = map(int, input().split())
        rowD, colD = map(int, input().split())
        res = bfs(rowS, colS, rowD, colD)
        print(res + 1)