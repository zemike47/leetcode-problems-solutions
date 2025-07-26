class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.first = self.second = self.prev = None
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            # Detect swapped nodes
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            
            self.prev = node
            inorder(node.right)
        
        inorder(root)
        # Swap the values of the two nodes
        self.first.val, self.second.val = self.second.val, self.first.val