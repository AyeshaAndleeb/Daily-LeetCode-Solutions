class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)  # Fast lookup
        forest = []

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None

            # Bottom-up processing
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            # If current node needs to be deleted
            if node.val in to_delete_set:
                if node.left:
                    forest.append(node.left)   # Add left child as new root
                if node.right:
                    forest.append(node.right)  # Add right child as new root
                return None  # Delete this node

            return node  # Keep this node

        root = dfs(root)
        if root:
            forest.append(root)  # Add root if it's not deleted

        return forest