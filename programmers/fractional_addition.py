import math

def solution(n1, d1, n2, d2):
    answer=[]
    
    number = d1 * n2 + n1 * d2
    demon = d1 * d2
    gcd = math.gcd(number,demon)
    answer = [number//gcd, demon//gcd]
   
    return print(answer)

solution(1,2,3,4)
