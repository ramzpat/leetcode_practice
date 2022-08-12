# https://leetcode.com/problems/design-add-and-search-words-data-structure/

from typing import Dict


class TrieNode: 
  def __init__(self):
    self.nextChars:Dict[str, TrieNode] = {}
    self.isWord = False

class WordDictionary:

  def __init__(self):
    self.rootTrie = TrieNode()

  def addWord(self, word: str) -> None:
    ptr = self.rootTrie
    for c in word:
      if c not in ptr.nextChars.keys():
        ptr.nextChars[c] = TrieNode()
      ptr = ptr.nextChars[c]
    ptr.isWord = True 

  def search(self, word: str) -> bool:
    stk = [(self.rootTrie, 0)]
    n = len(word)
    while len(stk) > 0:
      (ptr, char_index) = stk.pop()
      if char_index >= n and ptr.isWord: 
         return True
      elif char_index < n:
        char = word[char_index]
        if char == ".":
          for c in ptr.nextChars.keys():
            stk.append((ptr.nextChars[c], char_index + 1))
        else:
          if char in ptr.nextChars.keys():
            stk.append((ptr.nextChars[char], char_index + 1))
    return False 
          




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)