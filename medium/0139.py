# https://leetcode.com/problems/word-break/

from platform import node
from typing import Dict, List, Set, TypeVar

class TrieNode: 
  def __init__(self):
    self.matchWord = False
    self.child:Dict[str, self.TrieNode] = {} 
  
  def addWord(self, word:str):
    # Time Complexity: O(n)
    node_ptr = self
    for char in word:
      if char not in node_ptr.child:
        # create a new node if it doesn't exist
        node_ptr.child[char] = TrieNode()
      # Go to the next node
      node_ptr = node_ptr.child[char]

    # Mark that this is the added word 
    node_ptr.matchWord = True    
  
  def isMatch(self, word:str):
    node_ptr = self
    for char in word: 
      if char not in node_ptr.child:
        return False
      node_ptr = node_ptr.child[char]
    return node_ptr.matchWord

class Solution: 
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    # Prepare the trie for string matching
    root = TrieNode()
    for  word in wordDict:
      root.addWord(word)
    
    # Prepare a boolean flag to check if the string [0:i] match can be constructed from wordList 
    canBuild:List[bool] = [False] * (len(s) + 1)
    canBuild[0] = True
    for i in range(1, len(s)+1):
      
      # Check if previous s[:j] can be build using 'canBuild[j]' for any j in [0:i] and check the word s[j:i] can be build from the word list.
      for j in range(i):
        if (canBuild[j] and root.isMatch(s[j:i])):
          canBuild[i] = True 
          break 
    return canBuild[len(s)] 
  
# Test 
s = Solution()
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
print(s.wordBreak(s = "leetcode", wordDict = ["leet","code"]))

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
print(s.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))

