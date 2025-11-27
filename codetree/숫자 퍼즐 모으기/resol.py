N, M = map(int, input().split())
puzzles = [set(map(int, input().split())) for _ in range(N)]
import time

start = time.time()

print(puzzles)
visited = [False] * N

min_cnt = N
def dfs(picked, cnt):
    global min_cnt
    
    if cnt >=  min_cnt:
        return 
    
    if cnt == N: # 모든 숫자 세트를 선택한 경우
        return
    
    if len(picked) == 10:
        min_cnt = min(min_cnt, cnt)

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(picked|puzzles[i], cnt + 1)
            visited[i] = False

dfs(set(),0)
print(min_cnt)

end = time.time()

print("실행 시간:", end - start, "초")