"""
Problem: 별 찍기 - 7
URL: https://www.acmicpc.net/problem/2444
Input:
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
Output:
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
Example 1:
Input:
5

Output:
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *

"""

n = int(input())

for i in range(1, n+1):
    print(' '*(n-i)+'*'*(2*i-1))
for i in range(n-1, 0, -1):
    print(' '*(n-i) + '*'*(2*i-1))

