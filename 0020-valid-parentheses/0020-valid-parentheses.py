class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i == '[' or i == '(' or i == '{':
                stack.append(i)
            elif len(stack) != 0:
                if i == ']' and stack.pop() != '[':
                    return False
                elif i == ')' and stack.pop() != '(':
                    return False
                elif i == '}' and stack.pop() != '{':
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        return False
        """
        :type s: str
        :rtype: bool
        """
        