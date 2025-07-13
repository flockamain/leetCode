"""Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""
class Solution(object):
    def strStr(self, haystack, needle):
        h = list(haystack)
        n = list(needle)

        for i in range(len(h)):
            while i + len(n) <= len(h):
                if h[i:i + len(n)] == n:
                    return(i)
                i += 1
        else:
            return(-1)
