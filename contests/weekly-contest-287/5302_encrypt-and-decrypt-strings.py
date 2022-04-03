# https://leetcode.com/contest/weekly-contest-287/problems/encrypt-and-decrypt-strings/

class Encrypter(object):

    def __init__(self, keys, values, dictionary):
        """
        :type keys: List[str]
        :type values: List[str]
        :type dictionary: List[str]
        """
        self.key_hash = {}
        self.value_hash = {}
        for i in range(0, len(keys)):
            self.key_hash[keys[i]] = values[i]
            self.value_hash[values[i]] = keys[i]

        self.possible_encryted_words = {}
        for w in dictionary:
            encrypted_word = self.encrypt(w)
            if not (encrypted_word in self.possible_encryted_words):
                self.possible_encryted_words[encrypted_word] = 1
            else:
                self.possible_encryted_words[encrypted_word] += 1   

        

    def encrypt(self, word1):
        """
        :type word1: str
        :rtype: str
        """
        encrypted_word = ""
        for w in word1:
            encrypted_word = encrypted_word + (self.key_hash[w])
        return encrypted_word
        

    def decrypt(self, word2):
        """
        :type word2: str
        :rtype: int
        """
        if not (word2 in self.possible_encryted_words):
            return 0
        return self.possible_encryted_words[word2]
        


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)

encrypter = Encrypter(['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"])
ret = encrypter.encrypt("abcd"); # return "eizfeiam". 
                           # 'a' maps to "ei", 'b' maps to "zf", 'c' maps to "ei", and 'd' maps to "am".
ret = encrypter.decrypt("eizfeiam")
print(ret)