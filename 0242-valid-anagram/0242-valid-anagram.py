class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def count_chars(word):
            count = {}
            for i in word:
                if i in count:
                    count[i] += 1
                else:
                    count[i] = 1
            return count
        
        if count_chars(s) == count_chars(t):
            return True 
        return False


                
        