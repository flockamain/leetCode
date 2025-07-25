"""Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring."""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        start = 0
        max_len = 0
        max_substring = ""

        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[start])
                start += 1

            char_set.add(s[i])

            if i - start + 1 > max_len:
                max_len = i - start + 1
                max_substring = s[start:i + 1]

        return max_len