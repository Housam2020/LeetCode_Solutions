class Solution(object):
    def isPalindrome(self, s):
        #remove nonalphanumeric
        s2 = []
        for i in s:
            if i.isalpha():
                s2.append(i.lower())
            elif i.isdigit():
                s2.append(i)
        
        # read it backwards
        #keep pointers on each side
        i = 0
        j = len(s2)-1
        print(s2)
        while i <  j:
            if s2[i] != s2[j]:
                return False
            i+=1
            j-=1
        return True
        
        
        
        """
        :type s: str
        :rtype: bool
        """
        