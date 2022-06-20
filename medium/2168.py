# https://leetcode.com/problems/search-suggestions-system/

from typing import List 

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        searching_word = ""
        candidates = products[:]
        solution = []
        for w in searchWord:
          searching_word += w
          candidates = [candidate for candidate in candidates if candidate.startswith(searching_word)]
          candidates.sort()
          solution.append(candidates[:3])
        return solution
      

s = Solution()
print(s.suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"))