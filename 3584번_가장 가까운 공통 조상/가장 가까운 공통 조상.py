'''
문제:
    - 두 노드가 주어질때, 가장 가까운 공통 조상을 찾아라.
핵심 아이디어:
    -  나 자신도 나의 부모노드이자, 자식노드임.
'''

T = int(input())

for _ in range(T):
    N = int(input())
    parent = [0]*(N+1)

    for _ in range(N-1):
        A, B = map(int, input().split())
        parent[B] = A
        
    t1, t2 = map(int, input().split())

    t1_parent = set()
    cur = t1
    while cur != 0:
        t1_parent.add(cur)
        cur = parent[cur]

    cur = t2
    while cur not in t1_parent:
        cur = parent[cur]

    print(cur)        
