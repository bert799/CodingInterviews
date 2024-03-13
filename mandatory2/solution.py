# Do not modify the classes below
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, representation: str):
        '''
        representation: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        if not representation:
            return
        nodes = []
        for i, value in enumerate(representation):
            node = None
            if value is not None:
                node = TreeNode(value)
                if i > 0:
                    if i % 2 == 1:
                        parent = nodes[(i - 1) // 2]
                        parent.left = node
                    else:
                        parent = nodes[(i - 2) // 2]
                        parent.right = node
            nodes.append(node)
        self.root = nodes[0]


class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.adjacent = []


class Graph:
    def __init__(self, adjacency: list[list[bool]]):
        '''
        adjacency: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        self.nodes = [GraphNode(i) for i in range(1, len(adjacency) + 1)]
        for node1, row in zip(self.nodes, adjacency):
            for node2, adjacent in zip(self.nodes, row):
                if adjacent and node1 is not node2:
                    node1.adjacent.append(node2)


# Implement the functions below

def pre_order_recursive(root: TreeNode) -> None:
    if root:
        print(root.value)
        pre_order_recursive(root.left)
        pre_order_recursive(root.right)


def pre_order_iterative(root: TreeNode) -> None:
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            print(node.value)
            stack.append(node.right)
            stack.append(node.left)


def in_order_recursive(root: TreeNode) -> None:
    if root:
        in_order_recursive(root.left)
        print(root.value)
        in_order_recursive(root.right)


def post_order_recursive(root: TreeNode) -> None:
    if root:
        post_order_recursive(root.left)
        post_order_recursive(root.right)
        print(root.value)


def breadth_first(root: TreeNode) -> None:
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            print(node.value)
            queue.append(node.left)
            queue.append(node.right)


def graph_depth_first_recursive(node: GraphNode, visited=None) -> None:
    if visited is None:
        visited = set()
    # Your code goes here
    if node not in visited:
        visited.add(node)
        print(node.value)
        for adj in node.adjacent:
            graph_depth_first_recursive(adj, visited)


def graph_depth_first_iterative(node: GraphNode) -> None:
    stack = [node]
    visited = set()
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            print(current.value)
            stack.extend(current.adjacent)


def graph_breadth_first(node: GraphNode) -> None:
    queue = [node]
    visited = set()
    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.add(current)
            print(current.value)
            queue.extend(current.adjacent)
