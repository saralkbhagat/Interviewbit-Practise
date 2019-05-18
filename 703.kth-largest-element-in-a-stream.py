#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#
# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
#
# algorithms
# Easy (41.14%)
# Total Accepted:    13.7K
# Total Submissions: 33.3K
# Testcase Example:  '["KthLargest","add","add","add","add","add"]\n[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]'
#
# Design a class to find the kth largest element in a stream. Note that it is
# the kth largest element in the sorted order, not the kth distinct element.
# 
# Your KthLargest class will have a constructor which accepts an integer k and
# an integer array nums, which contains initial elements from the stream. For
# each call to the method KthLargest.add, return the element representing the
# kth largest element in the stream.
# 
# Example:
# 
# 
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
# 
# 
# Note: 
# You may assume that nums' length ≥ k-1 and k ≥ 1.
# 
#
class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.array=nums
        self.k=k
        heapq.heapify(self.array)
        while(len(self.array)>self.k):
            heapq.heappop(self.array)

        

    def add(self, val):
        if len(self.array)<self.k:
            heapq.heappush(self.array,val)
        elif self.array[0]<val:
            heapq.heapreplace(self.array,val)
        return self.array[0]

        """
        :type val: int
        :rtype: int
        """
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
