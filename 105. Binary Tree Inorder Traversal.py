"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        elements = []
        if root.left:
            elements += self.inorderTraversal(root.left)
        elements.append(root.val)
        if root.right:
            elements += self.inorderTraversal(root.right)
        return elements