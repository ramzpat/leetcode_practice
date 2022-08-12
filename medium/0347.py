# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter, defaultdict
from email.policy import default
from heapq import heapify, heappop, heappush, heappushpop
import random
from typing import Dict, List

class Solution:
  # Heap solution
  # O(n log(k))
  def heap_topKFrequent(self, nums: List[int], k: int) -> List[int]:
      # To count the frequency, we could use hash table 
      # To remember k top elements, heap solution
      
      # O(n)
      numsCnt = Counter(nums)

      # O(n log(k))
      heap_list = []
      for num in numsCnt:
        if len(heap_list) < k:
          heappush(heap_list, (numsCnt[num], num))
        elif numsCnt[num] > heap_list[0][0]:
          heappushpop(heap_list, (numsCnt[num], num))
      return [ num for (_, num) in heap_list] 
  
  # Hoare's selection algorithm
  # O(n^2)
  def quickselection_topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
    numsCnt = Counter(nums)
    unique_nums = list(numsCnt.keys())

    def partition(left:int, right:int, pivot:int) -> int:
      freq = numsCnt[unique_nums[pivot]]
      # 1. Move pivot to the end 
      unique_nums[pivot], unique_nums[right] = unique_nums[right], unique_nums[pivot]
      # 2. Partition
      store_index = left
      for i in range(left, right):
        if numsCnt[unique_nums[i]] < freq:
          unique_nums[i], unique_nums[store_index] = unique_nums[store_index], unique_nums[i]
          store_index += 1
      # 3. move the pivot 
      unique_nums[store_index], unique_nums[right] = unique_nums[right], unique_nums[store_index]
      return store_index

    def quick_selection(left, right, k_smallest):
      if left == right:
        return
      
      pivot = random.randint(left, right)
      pivot = partition(left, right, pivot)
      if pivot == k_smallest:
        return
      elif pivot < k_smallest:
        quick_selection(pivot+1, right, k_smallest)
      else: 
        quick_selection(left, pivot-1, k_smallest)

    n = len(unique_nums)
    quick_selection(0, n-1, n - k)
    return unique_nums[n-k:]

  # Bucket sort 
  # O(n)
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    cntNums = Counter(nums)
    n = len(nums)
    bucket:Dict[int, List[int]] = defaultdict(list)
    for num in cntNums:
      freq = cntNums[num]
      bucket[freq].append(num)
    ans = []
    for i in range(n, 0, -1):
      if len(ans) >= k:
        break 
      ans += bucket[i]
    return ans 