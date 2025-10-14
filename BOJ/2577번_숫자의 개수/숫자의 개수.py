"""
    - 문제: 
        - 3개의 자연수 입력이 주어짐
        - 3개의 숫자를 곱하였을때 0~9까지 각각 몇번쓰였는지
    - 시간복잡도:
        - 999*999*999 > N = 9(9자리 숫자)
        - 출력에 N 사용
    - idea:
        - 곱셈을 일단 하고, [0]*10 의 리스트에 해당 숫자 인덱스를 증가한다.
"""

A = int(input())
B = int(input())
C = int(input())

target = A*B*C
cnt_lst = [0]*10

for t in str(target):
    t = int(t)
    cnt_lst[t] += 1

for cnt in cnt_lst:
    print(cnt)