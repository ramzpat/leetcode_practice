# https://leetcode.com/contest/weekly-contest-303/problems/design-a-food-rating-system/

from collections import defaultdict
from heapq import heapify, heappop, heappush
from typing import Dict, List, Tuple


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
      self.foodRate:Dict[str, int] = {}
      self.foodList:Dict[str, List[Tuple[int, str]]] = {cuisine:[] for cuisine in cuisines}
      self.cuisineMap:Dict[str, str] = {}

      for i in range(len(foods)):
        self.foodRate[foods[i]] = ratings[i]
        self.cuisineMap[foods[i]] = cuisines[i]
        heappush(self.foodList[cuisines[i]], (-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
      self.foodRate[food] = newRating
      heappush(self.foodList[self.cuisineMap[food]], (-newRating, food))
      
      # Dispose old information
      (minus_rating, food) = heappop(self.foodList[self.cuisineMap[food]])    
      while self.foodRate[food] != -minus_rating:
        (minus_rating, food) = heappop(self.foodList[self.cuisineMap[food]])   
      heappush(self.foodList[self.cuisineMap[food]], (minus_rating, food)) 

    def highestRated(self, cuisine: str) -> str:
      (minus_rating, food) = heappop(self.foodList[cuisine])    
      # Dispose old information
      while self.foodRate[food] != -minus_rating:
        (minus_rating, food) = heappop(self.foodList[cuisine])    

      # Get all highest rated food 
      highest = minus_rating
      highest_list = [food]

      if len(self.foodList[cuisine]) > 0:
        (minus_rating, food) = heappop(self.foodList[cuisine])    
        while minus_rating == highest:
          highest_list.append(food)
          (minus_rating, food) = heappop(self.foodList[cuisine])    
        heappush(self.foodList[self.cuisineMap[food]], (minus_rating, food))

      highest_list.sort()
      val = highest_list[0]
      for food in highest_list:
        heappush(self.foodList[self.cuisineMap[food]], (highest, food))
      
      return val


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
foodRatings = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7])

# ["FoodRatings","highestRated","highestRated","changeRating","highestRated","changeRating","highestRated"]
# [[["kimchi","miso","sushi","moussaka","ramen","bulgogi"],["korean","japanese","japanese","greek","japanese","korean"],[9,12,8,15,14,7]],["korean"],["japanese"],["sushi",16],["japanese"],["ramen",16],["japanese"]]

print(foodRatings.highestRated("korean")) # return "kimchi"
                                    # "kimchi" is the highest rated korean food with a rating of 9.
print(foodRatings.highestRated("japanese")) # return "ramen"
                                      # "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); # "sushi" now has a rating of 16.
print(foodRatings.highestRated("japanese")) # return "sushi"
#                                       # "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); # "ramen" now has a rating of 16.
print(foodRatings.highestRated("japanese")) # return "ramen"
                                      # Both "sushi" and "ramen" have a rating of 16.
                                      # However, "ramen" is lexicographically smaller than "sushi".