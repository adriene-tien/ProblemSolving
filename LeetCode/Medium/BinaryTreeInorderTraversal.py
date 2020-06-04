# LeetCode Medium
# Binary Tree Inorder Traversal Question


class Solution:

    # recursive implementation: try the iterative implementation
    # Time complexity is O(n + n-1) -> O(n) where it is the addition of the number of nodes and edges
    # Space complexity: O(1)
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # left, root, right
        returnList = []

        def inorderTraversalRecursive(root, returnList):
            if not root:
                return
            inorderTraversalRecursive(root.left, returnList)
            returnList.append(root.val)
            inorderTraversalRecursive(root.right, returnList)

        inorderTraversalRecursive(root, returnList)
        return returnList
