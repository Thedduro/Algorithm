n, m = map(int, input().split())
words = input().split()

visited = [False] * n
result = '{'

def dfs(arr, length):
    global result

    if length > m:
        return
    if length == m:
        if arr < result:
            result = arr
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(arr + words[i], len(arr) + len(words[i]))
            visited[i] = False
    
dfs('',0)

if result != '{':
    print(result)
else:
    print(-1)