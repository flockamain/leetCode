"""Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]"""

nums = [3,2,3]

def majorityElement(self, nums):
    #no elements
    if not nums:
        return []
    #one element
    if len(nums) == 1:
        return [nums[0]]
    #two elements
    if len(nums) == 2 and nums[0] != nums[1]:
        return [nums[0], nums[1]]
    #if anything is more than this, it is added to the result
    size = len(nums) // 3
    #sort to make it easier to count
    nums.sort()
    #start of counter
    counter = 0
    #current number to compare to
    current = nums[0]
    #result array to return
    result = []
    #loop through array and count how many times each number appears.
    #if it is more than the size, add it to the result array
    for num in nums:
        if num == current:
            counter += 1
        #when we hit a new number we check the previous number
        #and reset the counter and current number to the new number
        else:
            if counter > size:
                result.append(current)
            current = num
            counter = 1
    #after the loop ends, check the last number
    if counter > size:
        result.append(current)
    return result

print(majorityElement(0, nums))
