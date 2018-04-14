'''
https://www.hackerrank.com/challenges/python-loops/problem
Task
Read an integer N. For all non-negative integers i< N , print i^2. See the sample for details.

Input Format
    The first and only line contains the integer, .

Constraints
    i <= N <= 20
Output Format
    Print  lines, one corresponding to each .

Sample Input 0
    5
Sample Output 0
    0
    1
    4
    9
    16

'''
num_a = int(raw_input())

# for each number between 1, num_a : range(1, num_a+1) e.g. for 1 2 3 4 5 can be written as range(1, 6), 6 is not inclusive
for index in range(1, num_a+1):
    print (index-1) * (index-1)
