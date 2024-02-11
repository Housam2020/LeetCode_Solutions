class Solution(object):
    def isAnagram(self, s, t):
        # use a hash aka dict in python
        anagram = {}
        for letter in s:
            if not anagram.get(letter):
                anagram[letter] = 1
            else:
                anagram[letter] += 1
        for letter in t:
            if not anagram.get(letter):
                return False
            if anagram.get(letter) == 0:
                return False
            else:
                anagram[letter] -= 1
        for num in anagram.values():
            if num > 0:
                return False
        return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        