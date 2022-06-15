# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

from collections import deque
from typing import List, Dict, Set, Tuple 

class Solution:

  
  def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    can_make:Dict[str, bool] = {supply:True for supply in supplies}
    required_supplies:Dict[str, List[str]] = {recipe: ingredient_l for recipe,ingredient_l in zip(recipes, ingredients) }
    
    def can_make_recipe(recipe:str) -> bool:
      if not (recipe in can_make):
        can_make[recipe] = False
        result = True
        for supply in required_supplies[recipe]:
          if (supply in supplies):
            pass 
          elif (supply in recipes) and not(supply == recipe):
            result = result and can_make_recipe(supply)
          else: 
            result = False
            break
        can_make[recipe] = result
      return can_make[recipe]


    return [recipe for recipe in recipes if can_make_recipe(recipe)]


s = Solution()
ret = s.findAllRecipes(['bread'], [["yeast","flour"]], ["yeast","flour","corn"])
print(ret)