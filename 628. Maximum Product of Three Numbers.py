"""Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6"""
nums = [-5,5,5,-5,-5,-5,0,1,2,3,-2,-3,-4]
def maximumProduct(self, nums):
    nums.sort(reverse=True)
    positiveNumber = 0
    finalNumbers = [1,2,3]

    print(nums)
    i = 0
    while i < 3:
        if nums[i] > 0:
            positiveNumber += 1
        i+=1
    print(positiveNumber)
    if positiveNumber == 0 and nums[0] == 0:
        return 0
    if len(nums) > 3:
        if positiveNumber == 0:
            nums.sort(key=abs, reverse=True)
            return nums[-1]*nums[-2]*nums[-3]
        if positiveNumber == 1:
            finalNumbers[0] = nums[0]
            nums.pop(0)
            nums.sort(key=abs, reverse=True)
            finalNumbers[1] = nums[0]
            finalNumbers[2] = nums[1]
            return finalNumbers[0]*finalNumbers[1]*finalNumbers[2]
        if positiveNumber == 2:
            finalNumbers[0] = nums[0]
            #get rid of both positives, so that we dont go negative
            nums.pop(0)
            nums.pop(0)
            nums.sort(key=abs,reverse=True)
            finalNumbers[1] = nums[0]
            finalNumbers[2] = nums[1]
            return finalNumbers[0]*finalNumbers[1]*finalNumbers[2]
        if positiveNumber >= 3:
            nums.sort(key=abs,reverse=True)
            if abs(nums[2]+nums[3]) == abs(nums[0]+nums[1]) and nums[2]+nums[3] != nums[0]+nums[1]:
                nums[2]=nums[2]*-1
                nums[3]=nums[3]*-1
            print(nums)
            finalNumbers[0] = nums[0]
            nums.pop(0)
            finalNumbers[1] = nums[0]
            nums.pop(0)
            print(nums)
            print(finalNumbers)
            if finalNumbers[0]*finalNumbers[1] > 0:
                for num in nums:
                    if num > 0:
                        finalNumbers[2] = num
                        print(finalNumbers)
                        break
            else:
                for num in nums:
                    if num < 0:
                        finalNumbers[2] = num
                        break
            return finalNumbers[0]*finalNumbers[1]*finalNumbers[2]
    else:
        return nums[0]*nums[1]*nums[2]
    
    
print(maximumProduct(0,nums))
