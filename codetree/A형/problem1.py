n, right = map(int, input().split())
left = 0
sky = [0] * (right+1)
for _ in range(n):
    i, t = map(int, input().split())
    sky[i] = t

cnt_left = 0
cnt_right = 0 

while left < right:
    if cnt_left == 0:
        if sky[left+1] != 0:
            cnt_left = sky[left+1]
        left += 1
    else:
        cnt_left -= 1
    
    if cnt_right == 0:
        if sky[right-1] != 0:
            cnt_right = sky[right-1]
        right -= 1
    else:
        cnt_right -= 1

print(left)