class Solution(object):
    def isAnagram(self, s, t):
        store = defaultdict(int)
        for i in s:
                store[i] += 1
        print(store)
        for j in t:
                store[j] -= 1
        for i in store:
            if store[i] != 0:
                return False
        return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        