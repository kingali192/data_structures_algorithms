class Node(object):
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data

# Recursive Algorithms
def preorder(self, root):
    if not root:
        return None
    
    res = []
    if root:
        res.append(root.data)
        res = self.preorder(root.left)
        res += self.preorder(root.right)
    return res 

def postorder(self, root):
    if not root:
        return None
    
    res = []
    if root:
        res = self.postorder(root.left)
        res += self.postorder(root.right)
        res.append(root.data)
    return res 

def inorder(self, root):
    if not root:
        return None
    
    res = []
    if root:
        res = self.inorder(root.left)
        res.append(root.data)
        res += self.inorder(root.right)
    return res  

# Iterative Algorithms

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    
    preorder(root) 
    postorder(root)
    inorder(root)   
    