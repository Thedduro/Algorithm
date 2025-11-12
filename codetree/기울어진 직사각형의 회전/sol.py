'''
- 문제: 
    - 특정 좌표 r,c 에서 상우 대각 > 상좌 대각 > 우좌 대각 > 우하 대각
    - 0 이면 반시계 방향으로 1칸, 1이면 시계방향으로 한칸
- 아이디어:
    - 리스트에 만들어지는 직사각형의 요소들의 좌표를 입력한 후, 로테이션 함.
    - 그리고 다 만들어지면, 해당 좌표에 다시 하나씩 그 요소들을 대입함.
'''

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())
r, c = r-1, c-1

rect_idx = [(r,c)]

for _ in range(m1):
    r, c = r-1, c+1
    rect_idx.append((r, c))

for _ in range(m2):
    r, c = r-1, c-1
    rect_idx.append((r, c))

for _ in range(m3):
    r, c = r-1, 