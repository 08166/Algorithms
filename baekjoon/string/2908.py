"""
Baekjoon Problem 2908: 상수 (Sangsue)

Problem Description:
Sang-geun's younger brother, Sang-su, is bad at math and has trouble reading numbers. 
To help him, Sang-geun gives him a problem comparing the size of numbers. 
Sang-geun writes two three-digit numbers on a chalkboard and asks Sang-su to say which one is larger.

The twist is that Sang-su reads numbers backward. For example, he reads 734 as 437.

Your program needs to take two three-digit numbers as input, reverse them as Sang-su would, 
and then print the larger of the two reversed numbers.

Input:
The input consists of a single line with two three-digit numbers, separated by a space.
These numbers will not be the same and will not contain a '0'.

Output:
Print the larger of the two numbers after they have been reversed.
"""

n, m = input().split()
n = int(n[::-1])
m = int(m[::-1])

if n > m :
    print(n)
else :
    print(m)