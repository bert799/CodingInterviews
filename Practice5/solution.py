from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> list[Optional[TreeNode]]:
        if not n % 2:
            return []
        elif n == 1:
            return [TreeNode(0)]
        else:
            result = []
            for k in range(1, n-1, 2):
                for l in self.allPossibleFBT(k):
                    for r in self.allPossibleFBT(n-1-k):
                        result.append(TreeNode(0, l, r))
            
            return result