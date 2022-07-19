# https://leetcode.com/problems/my-calendar-i/

class MyCalendar:

  def __init__(self):
    self.slot = []

  def book(self, start: int, end: int) -> bool:
    # Binary search O(log n)
    left, right = 0, len(self.slot)-1
    while left <= right:
      mid = (left + right)//2
      time_s, time_e = self.slot[mid]
      if end <= time_s:
        right = mid - 1
      elif start >= time_e:
        left = mid + 1
      else: 
        return False 
    # Concat array: O(n)? 
    self.slot = self.slot[:left] + [(start, end)] + self.slot[left:]
    return True 

s = MyCalendar()
print(s.book(10, 20))
print(s.book(15, 25))
print(s.book(20, 30))


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)