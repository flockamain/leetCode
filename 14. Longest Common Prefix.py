"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
    
        #min_length is essentially a number
        #min function returns the smallest item, so we get the minimum length
        min_length = min(len(s) for s in strs)

        #for each index i only going up to the minimum length, check if all
        #characters at that index are the same. If not, return the 
        #characters up to that index
        for i in range(min_length):
            # if characters at position i are not all the same, stop
            if len(set(s[i] for s in strs)) > 1:
                return strs[0][:i]
        #if they are all the same up to the minimum length, return the 
        #common characters up to the minimum length
        return strs[0][:min_length]
