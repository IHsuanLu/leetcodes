# we care about the index number in the longest substring problem
# every time we see "(", we put the index into a stack, while when we see ")", we pop the stack and check the index difference

# takeaways: we don't necessarily need sliding windows in parentheses questions
# the stack can help us simulate the slidings with correct timing of appending, popping, and indexing

# overall, parentheses problem is all about the followings
# - stack, append when seeing "(" and pop when seeing ")"
#    - keep in mind that the stack[-1], "(", should always match the incoming ")"
# - left, right count should be balance
# - right count should at no circumstance exceed the left count


# try thinking with the edge case ")()())"
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0
        
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                
                max_length = max(max_length, i - stack[-1])
        
        return max_length
