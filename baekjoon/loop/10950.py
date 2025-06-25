"""
문제 : 
    두 정수 A와 B를 입력받은 다음, A + B를 출력하는 프로그램을 작성하시오.
    
입렵 :
    첫째 줄에 테스트 케이스의 개수 T가 주어진다.
    각 테스트 케이스는 한 줄로 이어져 있으며, 각 줄에 A와 B가 주어진다. (0 < a, B < 10)

출력 : 
    각 테스트 케이스마다 A + B를 출력한다.
    
예제 입력 : 
        5
        1   1
        2   3
        3   4
        9   8
        5   2
        
예제 출력 : 
        2
        5
        7
        17
        7
"""

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    print(a+b)


# def solution(a,b,t):
#     return

# solution(5)
# solution(1,1)
# solution(2,3)
# solution(3,4)
# solution(9,8)
# solution(5,2)