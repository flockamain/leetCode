"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true"""
def containsDuplicate(self, nums):
    #create a set to store unique numbers
    unique = set()
    #if you used .count(), it would be 0(n^2)
    #but using a set is 0(n) because it runs through
    #the list once
    #i tried .count() first because it was simpler, but it was too slow :(
    for num in nums:
        if num in unique:
            return True
        else:
            unique.add(num)
    return False
