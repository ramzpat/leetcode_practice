from collections import Counter


class Solution:
  def largestPalindromic(self, num: str) -> str:
    cntNum = Counter(num)
    i = 9
    ans_even = []
    highest_odd_num = -1
    # clear pairs 
    is_leading_zero = True 
    while i >= 0:
      if is_leading_zero and i == 0:
        if cntNum[str(i)] >= 1 and highest_odd_num == -1:
          highest_odd_num = i
        break
      while cntNum[str(i)] > 1:
        ans_even.append(i)
        cntNum[str(i)] -= 2
        if i != 0:
          is_leading_zero = False 
      if cntNum[str(i)] == 1 and highest_odd_num == -1:
        highest_odd_num = i
      i -= 1 
    ans_str = "".join([ str(i) for i in ans_even ])
    if highest_odd_num != -1:
      ans_str += str(highest_odd_num)
      
    ans_str += "".join([ str(i) for i in ans_even[::-1] ])
      
    return ans_str

