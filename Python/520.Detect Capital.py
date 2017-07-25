'''
520. Detect Capital
'''
word = input("s=:")
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        i = 0
        if word[0].isupper():
            for j in word:
                if j.isupper():
                    i += 1
            if i == len(word) or i == 1:
                return True
            else:
                return False
        elif word[0].islower():
            for j in word:
                if j.islower():
                    i += 1
            if i == len(word):
                return True
            else:
                return False