"""Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

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

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701"""
def titleToNumber(self, columnTitle):
    #create mapping of letters to numbers
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
                   16,17,18,19,20,21,22,23,24,25,26]
        letters = ['A','B','C','D','E','F','G','H','I','J','K','L',
                     'M','N','O','P','Q','R','S','T','U','V','W','X',
                     'Y','Z']
        mapping = dict(zip(letters, numbers))
        
        #for each letter, multiply the result by 26 
        #and add the letter's number to the result
        #its like moving over a decimal place in base 10
        #and multiplying that place by 10, but in this case
        #we are moving over a base 26 place and multiplying by 26

        result = 0
        for letter in columnTitle:
            #the initial result of result*26 is 0, so the first letter will just add
            #its number, but after that, the result will be multiplied by 26
            #before adding the next letter's number, which is how we move over a base 26 place
            result = result * 26 + mapping[letter]
        return result
