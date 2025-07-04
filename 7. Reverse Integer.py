"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21"""
class Solution(object):
    def reverse(self, x):
        y = 0
        o = 0
        a = []
        if x < 0:
            y = -x
        elif x == 0:
            return 0
        else:
            y = x
        while y > 0:
            a.append(str(y % 10))
            y = y // 10
        o = str(''.join(a))
        o = int(o)
        if x < 0:   
            o = o*-1
        if o >2147483647 or o < -2147483648:
            o = 0
        return o