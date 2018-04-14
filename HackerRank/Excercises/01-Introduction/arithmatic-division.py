'''
Task
Read two integers and print two lines.
The first line should contain integer division,  a//b . The second line should contain float division,  a/b .
You don't need to perform any rounding or formatting operations.

Input Format
    The first line contains the first integer, . The second line contains the second integer, .

Output Format
    Print the two lines as described above.

Sample Input 0
    4
    3
Sample Output 0
    1
    1.33333333333
'''

num_a = int(raw_input())
num_b = int(raw_input())

#integer division
print num_a//num_b

#float division
print num_a * (1.0) / num_b
