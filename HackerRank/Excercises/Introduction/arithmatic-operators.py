'''
Task
Read two integers from STDIN and print three lines where:

1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.

Input Format
    The first line contains the first integer, . The second line contains the second integer, .

Constraints
    1 <= a < 10^10
    1 <= b <= 10^10

Output Format
    Print the three lines as explained above.
Sample Input 0
    3
    2
Sample Output 0
        5
        1
        6

'''

num_a = int(raw_input())
num_b = int (raw_input())

#print sum of 2 numbers:
print num_a + num_b

#print difference of two numbers (first - second)
print num_a - num_b

#print product of two numbers
print num_a * num_b
