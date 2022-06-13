# https://leetcode.com/problems/stock-price-fluctuation/
from typing import List, Dict

class StockPrice:

    def __init__(self):

        # timestamp, last_price  
        self.stock_last_p = {}

        # List of prices
        self.price_list = []

        # Last timestamp 
        self.last_timestamp = 0

    def __deletePrice(self, price:int):
        left, right = 0, len(self.price_list)-1
        while(left <= right):
            mid = int((left + right) / 2)
            if price == self.price_list[mid]:
                self.price_list = self.price_list[:mid] + self.price_list[mid+1:]
                return
            elif price > self.price_list[mid]:
                left = mid + 1
            else:
                right = mid - 1

    def __insertPrice(self, price:int):
        left, right = 0, len(self.price_list)-1
        while(left <= right):
            mid = int((left + right) / 2)
            if price == self.price_list[mid]:
                left = mid
                break
            elif price > self.price_list[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        if left >= len(self.price_list):
            self.price_list.append(price)
        elif left == 0:
            self.price_list = [price] + self.price_list
        elif price > self.price_list[left]:
            self.price_list = self.price_list[:left+1] + [price] + self.price_list[left+2:]
        else:
            self.price_list = self.price_list[:left] + [price] + self.price_list[left:]

    def update(self, timestamp: int, price: int) -> None:
        if not(timestamp in self.stock_last_p):
            self.stock_last_p[timestamp] = price
            self.__insertPrice(price)
            # print(self.price_list)
        else:
            old_price = self.stock_last_p[timestamp]
            self.stock_last_p[timestamp] = price

            self.__deletePrice(old_price)
            # print(self.price_list)
            self.__insertPrice(price)
            # print(self.price_list)
        
        if self.last_timestamp < timestamp:
            self.last_timestamp = timestamp

    def current(self) -> int:
        return self.stock_last_p[self.last_timestamp]

    def maximum(self) -> int:
        return self.price_list[-1]

    def minimum(self) -> int:
        return self.price_list[0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

obj = StockPrice()
obj.update(1, 10)
obj.update(2, 5)
print(obj.current())
print(obj.maximum())
obj.update(1, 3)
print(obj.maximum())
obj.update(4, 2)