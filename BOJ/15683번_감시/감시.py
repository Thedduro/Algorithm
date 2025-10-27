#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15683                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lsw2207@gmail.com <boj.kr/u/lsw2207@gmail   +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15683                          #+#        #+#      #+#     #
#    Solved: 2025/10/27 11:46:01 by lsw2207@gmail.###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

'''
- 문제:
    - 각 종류의 cctv가 감시할 수 있는 방향을 정의.
    - 이때, 벽이면 감시 불가.
    - cctv 방향을 내가 정해서
    - 사각지대의 최소 크기를 구한다.
- 아이디어:
    - cctv 종류에 따른 방향 정의
    - cctv가 가장 많이 볼 수 있는 방향을 정함.
'''

N, M = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(N)]

direction = [(0,1),(0,-1),(1,0),(-1,0)]
# CCTV별 가능한 방향 조합
cctv_dir = {
    1: [[0], [1], [2], [3]],
    2: [[0,1], [2,3]],
    3: [[0,2], [0,3], [1,2], [1,3]],
    4: [[0,1,2], [0,1,3], [0,2,3], [1,2,3]],
    5: [[0,1,2,3]]
}

cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= room[i][j] <= 5: 
            cctv.append((room[i][j],i,j))

def watch(temp, x, y, dirs):
    for d in dirs:
        nx, ny = x, y
        while True:
            nx += direction[d][0]
            ny += direction[d][1]
            if not (0 <= nx < N and 0 <= ny < M) or temp[nx][ny] == 6:
                break
            # 다른 CCTV는 통과 가능
            if temp[nx][ny] == 0:
                temp[nx][ny] = '#'

queue = []
queue.append((0, room))
min_4 = float('inf')

while queue:
    idx, current = queue.pop(0)

    if idx == len(cctv):
        cnt = sum(row.count(0) for row in current)
        min_4 = min(min_4, cnt)

        continue

    c_type, x, y = cctv[idx]

    for dirs in cctv_dir[c_type]:
        temp = [row[:] for row in current]
        watch(temp, x, y, dirs)
        queue.append((idx+1, temp))

print(min_4)