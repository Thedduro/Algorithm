'''
- 문제:
    - 겹치는 수는 없다...
    - 숫자 1부터 시작해서 8방향으로 인접한 칸 중에 가장 큰 수와 중앙 값을 교환
    - 1 ~ n^2 까지 순차적으로 이동 
    > 여기까지 한턴 총  m턴을 돌았을때 상태를 출력해라
- 아이디어:
    - m번을 반복하면서, n^2을 돌면서 모든 값의 위치좌표를 저장
    - 그리고 8방향을 돌면서 최대 값과 최대 인덱스를 찾고 교환
    - 이때 위치좌표의 정보도 교환
- 시간복잡도:
    - 100*(400 + 400*8)
'''

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

direction = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def get_idx():
    dict = {}
    for i in range(n):
        for j in range(n):
            dict[grid[i][j]] = (i,j)
    return dict

for _ in range(m):
    dict = get_idx()
    for num in range(1, n*n+1):
        x,y = dict[num]
    
        max_num = 0
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n:
                next_num = grid[nx][ny]
                if next_num > max_num:
                    max_num = next_num
                    max_x, max_y = nx, ny

        # 인덱스 사전 변경
        dict[num] = (max_x, max_y)
        dict[max_num] = (x,y)
        # 그리드 변경
        grid[x][y] = max_num
        grid[max_x][max_y] = num

for row in grid:
    print(*row)
        

