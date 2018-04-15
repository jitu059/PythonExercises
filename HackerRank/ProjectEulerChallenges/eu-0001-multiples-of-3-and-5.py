'''
https://www.hackerrank.com/contests/projecteuler/challenges/euler001
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of  3 or 5 below N.

Input Format
    First line contains  that denotes the number of test cases. This is followed by  lines, each containing an integer, .
Constraints
    1 <= T <= 10^5
    1 <= N <= 10^9
Output Format
    For each test case, print an integer that denotes the sum of all the multiples of 3 or 5 below N.

'''

import sys

#Lambda function to check if a arg_num is multiple of arg_mul_of or not
is_mul_of_ = lambda arg_num, arg_mul_of: True if arg_num % arg_mul_of == 0 else False

'''
# can be solved like this too
def _sum_of_mul_3_or_5(_arg_num):
    _sum = 0
    for each_num in range(0, _arg_num):
        if is_mul_of_(each_num, 3) or is_mul_of_(each_num, 5):
            _sum += each_num
    return _sum

'''
#List comprehension with lambda to get sum of all the numbers which are multiple of 3 or 5 in the range of _arg_num
def _sum_of_mul_3_or_5(arg_num):
    _r_sum = 0
    #Get the list of numbers which are multiple of either 3 or 5 in the range arg_num
    _sum_of = [each_num for each_num in range(0, arg_num) if is_mul_of_(each_num, 3) or is_mul_of_(each_num, 5) ]

    #add the items in the list to get the sum of numbers which are multiple of 3 or 5 in the range of arg_num
    _r_sum = reduce((lambda item_a, item_b: item_a + item_b ), _sum_of)
    return _r_sum

t = int(raw_input().strip())
_total_sum = 0

for a0 in range(t):
    n = int(raw_input().strip())
    _each_sum = _sum_of_mul_3_or_5(n)
    _total_sum += _each_sum

print _total_sum
