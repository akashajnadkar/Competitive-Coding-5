"""
Time Complexity - O(n)
Space Complexity - O(n/2) for BFS or O(h) i.e. O(logn)

Works on leetcode
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def __init__(self):
        self.result = []
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        #DFS
        self.dfs(root, 0)

        #BFS
        #Doing levelwise traversal of Tree
        # nodeQ = deque()
        # result = []
        # nodeQ.append(root) #push the root in the queue
        # while nodeQ:
        #     size = len(nodeQ)
        #     maxVal = -2**31 #create a default maxValue for each row
        #     We only want to consider nodes that belong to that particular level hence we have a for loop
        #     for i in range(size):
        #         node = nodeQ.popleft()
        #         maxVal = max(maxVal, node.val) #compare the node value with maxValue and update if greater than maxValue

                  #add children to queue(if there are any)
        #         if node.left!=None:
        #             nodeQ.append(node.left)
        #         if node.right!=None:
        #             nodeQ.append(node.right)
              #append the final maxValue in the result array where each index represents level
        #     result.append(maxVal)
        return self.result

    def dfs(self, root, level):
        #while doing dfs we have maintain which level we are at
        if root == None:
            return
        #if we have not created a max for a particular level, add it to result array
        if level == len(self.result):
            self.result.append(root.val)
        #if created then compare the values
        else:
            self.result[level] = max(self.result[level],root.val)
        #Finally traverse to the children with an increased level
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)
