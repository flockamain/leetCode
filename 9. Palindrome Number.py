"""Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome."""


class Solution(object):
    def isPalindrome(self, x):
        myarray = []
        tester = 0
        if x < 0:
            return False
        if x == 0:
            return True
        while x > 0: 
            myarray.append(x %10)
            x = x // 10
        for i in range(len(myarray)):
            if myarray[i] != myarray[len(myarray) - 1 - i]: 
                tester = 0
                break
            else:
                tester = 1
        if tester == 1:
            return True
        else:
            return False