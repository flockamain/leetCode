"""Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false"""

s = "ahbc"
t = "ahbgdc"

def isSubsequence(self, s, t):
    indexer = 0

    if len(s) == 0:
        return True

    for char in t:
        if char == s[indexer]:
            indexer+=1
        if indexer == len(s):
            return True
    return False

print(isSubsequence(0,s,t))