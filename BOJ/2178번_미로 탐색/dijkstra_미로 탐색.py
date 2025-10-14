N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

import heapq

def dijkstra():
    INF = 10**9
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = [[INF]*M for _ in range(N)]
    visited[0][0] = 0 # 시작지점 초기화

    heap = []
    heapq.heappush(heap,(0,0,1))

    while heap:
        x, y, weight = heapq.heappop(heap)

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if board[nx][ny] == 0: continue
            else:
                if weight + 1 < visited[nx][ny]:
                    visited[nx][ny] = weight + 1
                    heapq.heappush(heap,(nx, ny, weight+1))
    return visited

print(dijkstra()[-1][-1])