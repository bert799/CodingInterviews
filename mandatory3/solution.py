# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        self.tgt_sum = targetSum
        self.count = 0
        self.hash_map = {0:1}
        self.percorreNos(root, 0)
        return self.count
    def percorreNos(self, root, path_val):
        if not root:
            return
        path_val += root.val
        self.count += self.hash_map.get(path_val - self.tgt_sum, 0)
        self.hash_map[path_val] = self.hash_map.get(path_val, 0) + 1
        self.percorreNos(root.left, path_val)
        self.percorreNos(root.right, path_val)
        #print(path_val - self.tgt_sum)
        self.hash_map[path_val] -= 1