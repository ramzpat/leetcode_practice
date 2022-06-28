# https://leetcode.com/problems/stock-price-fluctuation/
from heapq import heappop, heappush
from typing import List, Dict


class StockPrice:

    def __init__(self):

        # timestamp, last_price  
        self.stock_last_p = {}

        # List of prices
        self.price_min = []
        self.price_max = []

        # Last timestamp 
        self.last_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        self.stock_last_p[timestamp] = price
        if self.last_timestamp < timestamp:
            self.last_timestamp = timestamp
        heappush(self.price_min, (price, timestamp))
        heappush(self.price_max, (-price, timestamp))

    def current(self) -> int:
        return self.stock_last_p[self.last_timestamp]

    def maximum(self) -> int:
        price, timestamp = heappop(self.price_max)
        while -price != self.stock_last_p[timestamp]:
            price, timestamp = heappop(self.price_max)
        heappush(self.price_max, (price, timestamp))
        return -price 

    def minimum(self) -> int:
        price, timestamp = heappop(self.price_min)
        while price != self.stock_last_p[timestamp]:
            price, timestamp = heappop(self.price_min)
        heappush(self.price_min, (price, timestamp))
        return price 


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