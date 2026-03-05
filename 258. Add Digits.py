"""Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0"""
def addDigits(self, num):
    # convert the number to a string
    num = str(num)
    #while the length of the number is greater than 1, keep adding the digits together
    while len(num) > 1:
        #convert the number into a string once again, but that string is the sum of
        #the digits in the original number
        num = str(sum([int(x) for x in num]))
    return int(num)
print(addDigits(0,38))
