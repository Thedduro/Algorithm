'''
- 문제:
    - K=한번에 이동가능 최대 정류장, N=총 정류장수, M=충전기 개수
- 아이디어:
    - 우선, 한번에 이동가능한 정류장 > 작은 수로 진행하며 제일 먼 거리의 충전기에서 충전함

'''

import sys
sys.stdin = open('sample_input.txt','r')

def solve(K, N, charger):
    curr = 0 
    cnt = 0
    while curr <= N:
        flag = False
        for i in range(K+curr, curr, -1):
            if i == N: 
                return cnt
            if i in charger:
                cnt += 1
                curr = i
                flag = True
                break
        if not flag:
            return 0

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))
    print(f'#{tc}', solve(K, N, charger))