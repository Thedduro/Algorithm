'''
- 문제: 
    - m개이상 연속으로 같은 숫자가 적혀있는 폭탄들을 제거
    - 계속 반복되다가 최종적으로 터질 폭탄들이 남을때까지 계속 진행
- 아이디어:
    - 다른 숫자가 나올때 까지 계속 스택에 쌓다가 m 이상이면 다 제거
    - 마지막 요소는 스택에 넣고 
'''
n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums = nums[::-1]

while True:
    new = []
    removed = False
    i = 0

    while i < len(nums):
        j = i
        # j까지 연속된 구간 찾기
        while j < len(nums) and nums[j] == nums[i]:
            j += 1
        
        length = j - i

        # M개 이상이면 해당 구간 전체 제거
        if length >= m:
            removed = True
        else:
            # 남겨야 하는 구간
            new.extend(nums[i:j])

        i = j

    nums = new[:]  # 제거 후 남은 폭탄들로 교체

    if not removed:   # 더 이상 터질 게 없으면 종료
        break

# 출력
print(len(nums))
for x in nums[::-1]:
    print(x)