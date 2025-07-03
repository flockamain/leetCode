"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true"""

class Solution(object):
    def isValid(self, s):
        z = list(s)
        d = []

        for i in range(len(z)):
            h = z[i]
            next = z[i + 1] if i + 1 < len(z) else None
            if h == "(" or h == "[" or h == "{":
                d.append(h)
            elif h == ")" or h == "]" or h == "}":
                if not d:
                    return False
                    break
                top = d.pop()
                if (h == ")" and top != "(") or \
                (h == "]" and top != "[") or \
                (h == "}" and top != "{"):
                    return False
                    break
        if not d:
            return True
        if len(d) > 0:
            return False