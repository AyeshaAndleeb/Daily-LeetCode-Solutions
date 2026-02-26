class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0  # global max diameter store karega

        def height(node):
            # Agar node None hai to height 0
            if not node:
                return 0

            # Left subtree ki height
            left_height = height(node.left)
            # Right subtree ki height
            right_height = height(node.right)

            # Current node se diameter update karo
            # (left + right) = longest path through this node
            self.diameter = max(self.diameter, left_height + right_height)

            # Height return karo (current node ka)
            return 1 + max(left_height, right_height)

        height(root)
        return self.diameter