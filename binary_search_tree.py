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
    
    
            