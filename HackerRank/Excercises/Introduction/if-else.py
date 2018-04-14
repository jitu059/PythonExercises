'''
https://www.hackerrank.com/challenges/py-if-else/problem
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5 , print Not Weird
If  is even and in the inclusive range of 6  to 20 , print Weird
If  is even and greater than 20 , print Not Weird

Input Format:
    A single line containing a positive integer, .

Constraints:
    1 <= n <= 100


'''

input_n = raw_input()
input_n = int(input_n) # at this stge we assume integer input is given. We will see validation in later examples

if input_n % 2 != 0:
    print 'Weird'
else:
    if input_n >= 2 and input_n <= 5:
        print 'Not Weird'
    elif input_n >=6 and input_n <= 20:
        print 'Weird'
    else:
        print 'Not Weird'

        
