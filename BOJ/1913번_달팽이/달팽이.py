#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1913                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lsw2207 <boj.kr/u/lsw2207>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1913                           #+#        #+#      #+#     #
#    Solved: 2025/10/15 22:38:53 by lsw2207       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

'''
    - 문제:
        - N*N의 행렬에서 N**2 부터 1까지 채워야함.
        - 큐에 첫번째부터, 만약 방향이 넘어가면 다음 방향으로 이동
'''

N = int(input())
target = int(input())
snail = [[0] * N for _ in range(N)]

direction = {'d':(1,0),'r':(0,1),'u':(-1,0),'l':(0,-1)}
next_dir = {'d':'r','r':'u','u':'l','l':'d'}

queue = []
queue.append((0,0,'d'))
num = N**2

while queue:
    x, y, dir = queue.pop()
    if num == target:
        result = [x+1, y+1]
    snail[x][y] = num
    num -= 1

    if num <= 0:
        break

    # 이동
    dx, dy = direction[dir]
    nx, ny = x + dx, y + dy

    if 0<=nx<N and 0<=ny<N and snail[nx][ny] == 0:
            queue.append((nx,ny,dir))
    else:
        dx, dy = direction[next_dir[dir]]
        nx, ny = x + dx, y + dy
        queue.append((nx,ny,next_dir[dir]))

for p in snail:
    print(*p)

print(*result)
