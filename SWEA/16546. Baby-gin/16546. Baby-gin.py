'''
※ SW expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.

0~9 사이의 숫자 카드에서 임의의 카드 6 장을 뽑았을 때 , 3 장의 카드가
연속적인 번호를 갖는 경우를 run 이라 하고 , 3 장의 카드가 동일한 번호를 갖는
경우를 triplet 이라고 한다

그리고 , 6 장의 카드가 run 과 triplet 로만 구성된 경우를 baby gin 으로 부른다

6 자리의 숫자를 입력 받아 baby gin 여부를 판단하는 프로그램을 작성하라

[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=10

두번째줄에는 6장의카드의 숫자들이 주어진다.(예: 123456)
숫자는 1<=N<=9 이다

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 베이비진인경우 true, 아닌경우 false를 출력한다.
'''
import sys
sys.stdin = open("input.txt", "r")

def solve(numbers):
    for num in numbers:
        if numbers.count(num) >= 3:
            for _ in range(3):
                numbers.remove(num)
        if len(numbers) == 0:
            return 'true'
    
    numbers.sort()
    for _ in range(len(numbers)//3):
        v = min(numbers)
        if v+1 in numbers and v+2 in numbers:
            for _ in range(3):
                numbers.remove(v)
                v += 1
        if len(numbers) == 0:
            return 'true'

    return 'false'

T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().strip()))

    print(f'#{tc} {solve(numbers)}')