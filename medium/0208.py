# https://leetcode.com/problems/implement-trie-prefix-tree/

from collections import defaultdict
from typing import Dict, List, TypeVar


class TrieNode:
  def __init__(self, char:str):
    self.char = char 
    self.nextChar:Dict[str, TrieNode] = {}
    self.isWord = False 

class Trie:

    def __init__(self):
      self.root:TrieNode = TrieNode("")
      
    def insert(self, word: str) -> None:
      ptr = self.root
      for w in word: 
        if w not in ptr.nextChar:
          ptr.nextChar[w] = TrieNode(w)
        ptr = ptr.nextChar[w]
      ptr.isWord = True 

    def search(self, word: str) -> bool:
      ptr = self.root
      for w in word:
        if w not in ptr.nextChar: 
          return False 
        ptr = ptr.nextChar[w]
      return ptr.isWord

    def startsWith(self, prefix: str) -> bool:
      ptr = self.root
      for w in prefix:
        if w not in ptr.nextChar: 
          return False 
        ptr = ptr.nextChar[w]
      return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)