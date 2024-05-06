class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        i = 0
        vowel = 0
        consonant = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for letter in word:
            i += 1
            asc_code = ord(letter)
            if (asc_code < 48) or (asc_code > 58 and asc_code < 65) or (asc_code > 90 and asc_code < 97) or asc_code > 122:
                return False
            if (asc_code >=65 and asc_code <= 90) or (asc_code >= 97 and asc_code <= 122):
                if letter in vowels:
                    vowel = 1
                else:
                    consonant = 1
                        
        if i < 3:
            return False
        if vowel and consonant:
            return True
        else:
            return False
obj = Solution()
word = "234Adas"
result = obj.isValid(word)
print(result)