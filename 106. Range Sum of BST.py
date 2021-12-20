"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
"""


def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        out = self.findElements(root, 0, low, high)
        return out
        
        
    def findElements(self, node, output, low, high):
        if node.val >= low and node.val <= high:
            output += node.val
        if node.left is not None and node.val >= low:
            output = self.findElements(node.left,output,low,high)
        if node.right is not None and node.val <= high:
            output = self.findElements(node.right,output,low,high)
        
        return output
        
