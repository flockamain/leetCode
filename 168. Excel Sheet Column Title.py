"""Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"""
def convertToTitle(self, columnNumber):
        #create mapping of numbers to letters
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
                   16,17,18,19,20,21,22,23,24,25,26]
        letters = ['A','B','C','D','E','F','G','H','I','J','K','L',
                     'M','N','O','P','Q','R','S','T','U','V','W','X',
                     'Y','Z']
        mapping = dict(zip(numbers, letters))
        #if the column number is just one letter, return the letter
        if columnNumber <= 26:
            columnNumber = mapping[columnNumber]
            return columnNumber
        #if not, first find the last letter
        else:
            result = []
            while columnNumber > 0:
                 endNumber = columnNumber % 26
                 if endNumber == 0:
                     endNumber = 26
                #append the letter to the result list - dividing by 26 will
                #give the next letter
                 result.append(mapping[endNumber])
                 columnNumber = (columnNumber - endNumber) // 26
                 #these letters are reversed at this point, so
                 #reverse the result list and join to get the column title
            return ''.join(result[::-1])
