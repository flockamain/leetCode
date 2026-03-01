"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]"""

def letterCombinations(self, digits):
    #id like these split up into a list so i can loop through them
    digits = list(digits)
    #missing digits check
    if not digits:
        return []
    #mapping of numbers to letters
    numbers = [2, 3, 4, 5, 6, 7, 8, 9]
    letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    mapping = dict(zip(numbers, letters))
    temp = []
    #add the possible letters to a temporary list
    for i in digits:
        temp.append(mapping[int(i)])
    #loop through the list of possible letters and add them to the final list
    final = []
    for i in range(len(temp)):
        #on initial loop, add the first set of letters to the final
        #list, getting either 3 or 4 letters depending on the number.
        if i == 0:
            final = list(temp[i])
        else:
            new_final = []
            for j in final:
                for k in temp[i]:
                    #combine the letters from the initial loop
                    #with the letters from the temp list, and 
                    #add them to the new_final list
                    new_final.append(j + k)
            final = new_final
    return final
