'''
문제:
    - 카드는 1...N까지의 번호가 순서대로 존재.
    - 다음을 반복 실행함
        - 맨위의 카드를 버린다.
        - 제일 위 카드를 제일 아래로 옮긴다.
    - N이 주어질때, 가장 마지막에 남는 카드를 구한다.
아이디어:
    - 데크로 구현, while 문을 돌면서 반복
        - 변수 하나를 1로 지정해두고 1이면 > 버림 > 변수 = 2
        - 변수가 2이면 > 카드 옮김 > 변수 = 1
    - 카드 개수가 1이 될때 까지 반복
시간: 
    - N = 500,000
    - 데크로 구현하면 > 500000
'''

from collections import deque

N = int(input())
cards = deque()
for n in range(1, N+1): cards.append(n)

card_len = N # len() 계산 > O(N) > 개수 변수를 만들어서 시초 줄임
order = 1

while card_len > 1:
    if order == 1:
        cards.popleft()
        order += 1
        card_len -= 1
    else:
        temp = cards.popleft()
        cards.append(temp)
        order -= 1

print(cards.popleft())
