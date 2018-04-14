'''
https://www.hackerrank.com/challenges/python-print/problem
Read an integer N.
Without using any string methods, try to print the following:
123...N
Note that "..." represents the values in between.

Input Format

The first line contains an integer N.

Output Format

Output the answer as explained in the task.

Sample Input 0
    3
Sample Output 0
    123

'''
from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    counter = 1
    while counter <= n:
        print(counter, end='') # telling python print function to end the print with null string and not new line
        counter = counter+1
