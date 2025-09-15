"""
    - 문제:
        - 1로 연결되어 있는 그림의 개수, 그림의 크기 중 최대 값을 구해라.
        - 상하좌우로만 이동 가능. 한 노드에 다시 갈 이유는 전혀 없다
        - N = 500 > 완탐시 250,000
    - IDEA:
        - BFS로 풀어본다. (왜냐하면, 연습해야 하니까!!!!!!!)
        - visited를 사용해, 한번 간 곳은 다시 가지는 않는다
        - 0이거나, 배열을 넘어간 경우 가지 않는다. 
"""

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(board)