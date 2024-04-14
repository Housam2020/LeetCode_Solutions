class Solution(object):
    def isValid(self, s):

        bb = []
        for i in s:
            if i in ['(','[','{']:
                bb.append(i)
            else:
                # empty list
                if not bb:
                    return False
                x = bb.pop()
                if x == '(' and i != ')':
                    return False
                if x == '{' and i != '}':
                    return False
                if x == '[' and i != ']':
                    return False
        # gone through whole loop, make sure stack is empty 
        if bb:
            return False
        return True



        """
        :type bb: str
        :rtype: bool
        """
        