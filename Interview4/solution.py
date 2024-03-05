class TreeNode:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def in_order_succ(node: TreeNode) -> TreeNode:
    if not node:
        return None
    if node.right:
        return left_most_child(node.right)
    else:
        q = node
        x = q.parent
        while x and x.left != q:
            q = x
            x = x.parent
        return x
    
def left_most_child(node: TreeNode) -> TreeNode:
    if not node:
        return None
    while node.left:
        node = node.left
    return node