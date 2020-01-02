class Node(object):
    def __init__(self):
        self.data = data
        self.root = root
        self.left = left       
        self.right = right      
        
    # Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
                
    def preorder(self, root):
        res = []
        if root:
            res.append(root.val)
            res = self.preorder(root.left)
            res = res + self.preoder(root.right)
        return res
    
    def inorder(self, root):
        res = []
        if root:
            res = self.preorder(root.left)
            res.append(root.val)
            res = res + self.preoder(root.right)
        return res
    
    def postorder(self, root):
        res = []
        if root:
            res = self.preorder(root.left)
            res = res + self.preoder(root.right)
            res.append(root.val)
        return res
    
    def inorder_iterative(self, root):
        if not root:
            return
        
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.value)
                node = node.right
    
    def preorder_iterative(self, root):
        if not root: 
            return
        
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            result.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
    
    def postorder_iterative(self, root):
        if not root:
            return    
        visited = set()
        stack = []
        node = root
        
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                
                if node.right and not node.right in visited:
                    stack.append(node)
                    node = node.right
                else:
                    visited.add(node)
                    result.append(node.value)
                    node = None
    
    
    
    
    
            