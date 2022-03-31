# https://leetcode.com/problems/snapshot-array/
class SnapshotArray(object):

    # Hash table for each array index. 
    array_history = {}
    # The snapshot id 
    ongoing_snap_id = -1
    
    def __init__(self, length):
        """
        :type length: int
        """
        self.array_history = {}
        self.ongoing_snap_id = 0
        for index in range(0, length):
            # Create a history for each index
            # The value shall be (0, ongoing_snap_id+1) 
            self.array_history[index] = [(0, self.ongoing_snap_id)]

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        _, snap_id = self.array_history[index][-1]
        if (snap_id == self.ongoing_snap_id):
            self.array_history[index][-1] = (val, self.ongoing_snap_id)
        else:
            self.array_history[index].append(((val, self.ongoing_snap_id)))

    def snap(self):
        """
        :rtype: int
        """
        self.ongoing_snap_id = self.ongoing_snap_id + 1
        return self.ongoing_snap_id - 1
        

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        def bi_search(start, end):
            array_index = (end-start+1)/2 + start
            (val, s_id) = self.array_history[index][array_index]
            if (s_id == snap_id) or (start == end):
                return val
            elif (s_id > snap_id):
                return bi_search(start, array_index-1)
            else: 
                return bi_search(array_index, end)
        
        left, right = 0, len(self.array_history[index])-1
        ret = 0
        while (left <= right):
            mid = (left+right)/2
            (val, s_id) = self.array_history[index][array_index]
            if 
        return bi_search(0, len(self.array_history[index])-1)

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index, snap_iparam_2)

obj = SnapshotArray(3)
obj.set(0, 5)
param_2 = obj.snap()
obj.set(0, 6)
param_2 = obj.snap()
obj.set(0, 7)
obj.set(1, 7)
param_2 = obj.snap()
obj.set(0, 8)
param_3 = obj.get(1, 4)
print(param_3)

# obj = SnapshotArray(7)
# obj.set(0, 4)
# obj.set(3, 3)
# obj.snap()
# obj.set(0, 6)
# param_3 = obj.get(0,0)
# print(param_3)