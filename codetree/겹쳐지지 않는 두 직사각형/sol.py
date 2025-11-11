# 겹치지 않는 두 직사각형 (완전탐색 풀이)
# 시간복잡도: O((N^2 * M^2)^2) ≈ N^4 M^4 (비효율적이지만 개념용)
# N, M <= 6~7 정도면 충분히 동작 가능
# prefix sum으로 각 영역 합 O(1) 계산


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 누적합 계산
prefix = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[i][j] = grid[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
        # 현재 칸의 누적합 = 현재 칸 + 위쪽 + 왼쪽 - 겹친 부분 빼기

# 직사각형 합 계산 함수
def rect_sum(x1, y1, x2, y2):
    return prefix[x2+1][y2+1] - prefix[x1][y2+1] - prefix[x2+1][y1] + prefix[x1][y1]
    # 전체에서 위쪽 빼고, 왼쪽 빼고, 겹친 부분은 다시 더해줘야, 내가 원한 직사각형의 합 구해짐


# 모든 직사각형 후보
rects = []
for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1, n):
            for y2 in range(y1, m):
                total = rect_sum(x1, y1, x2, y2)
                rects.append((total, x1, y1, x2, y2))

# 두 직사각형이 겹치는지 확인
def overlap(a, b):
    _, ax1, ay1, ax2, ay2 = a
    _, bx1, by1, bx2, by2 = b
    # 하나라도 완전히 분리되어 있으면 겹치지 않음
    return not (ax2 < bx1 or bx2 < ax1 or ay2 < by1 or by2 < ay1)

# 두 직사각형 조합 중 최댓값
rects.sort(reverse=True)  # 큰 값부터 비교하면 조금 더 빠름
ans = -float('inf')
for i in range(len(rects)):
    for j in range(i+1, len(rects)):
        if not overlap(rects[i], rects[j]):
            ans = max(ans, rects[i][0] + rects[j][0])

print(ans)

'''
1. n,m 은 5 > 전체 직사각형의 케이스를 구해야함
 구하면서 stack에 추가할건데 좌측 상단 좌표와 , 우측 하단 좌표를 포함하여 리스트 형식으로 extend 진행

2. 구해진 stack 에서 stack[0] 값을 기준으로 sort를 진행함
> def check 함수를 구해서 최댓값 2개를 빼낼건데 , 최댓값부터 한다음 이제 check해서 겹치는지 확인 
'''