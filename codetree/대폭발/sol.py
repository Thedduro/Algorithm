'''
- 문제:
    - t초의 폭탄의 위치 r,c에서 
    - +1 초가 되면 4방향으로 폭탄이 생김
    - 근데 여기서 규칙! > 2^(t-1)의 거리 만큼 네 방향으로....
    - 기존 위치에 있던 폭탄은 그래도 남아있고 계속 터짐
    - m초가 되었을때 폭탄의 총 개수
'''

n, m, r, c = map(int, input().split())

# queue = deque([])
# visited = set()
# queue.append((r-1,c-1,0))
# visited.add((r-1,c-1))
# cnt = 1

# direction = [(-1,0),(1,0),(0,1),(0,-1)]
# while queue:
#     x, y, t = queue.popleft()
#     print(f"현재 위치: ({x+1}, {y+1}), 시간: {t}, 폭탄 개수: {cnt}")
#     if t == m:
#         break

#     for dx, dy in direction:
#         dx, dy = dx*(2**t), dy*(2**t)
#         nx, ny = x+dx, y+dy
#         print(f"  방향: ({dx}, {dy}), 새로운 위치: ({nx+1}, {ny+1})")
#         if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited:
#             queue.append((nx,ny,t+1))
#             visited.add((nx,ny))
#             cnt += 1
#     queue.append((x,y,t))

#     print(f"큐 상태: {list(queue)}")
# print(cnt)
r, c = r-1, c-1
bombs = [(r,c)]
visited = set()
visited.add((r,c))
cnt = 1

direction = [(-1,0),(1,0),(0,1),(0,-1)]

for t in range(m):
    curr = bombs[:]
    new = []
    for x, y in curr:
        for dx, dy in direction:
            dx, dy = dx*(2**t), dy*(2**t)
            nx, ny = x+dx, y+dy

            if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited:
                new.append((nx,ny))
                visited.add((nx,ny))
                cnt += 1
    bombs.extend(new)
print(cnt)