class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def heightAndSize(node,size):
    if(node is None):
        return 0

    l= heightAndSize(node.left,size)
    r = heightAndSize(node.right,size)

    size[0] = size[0]+1

    return l+1 if (l>r) else (r+1)

def density(root):
    if(root == None):
        return 0
    size = [0]
    height  = heightAndSize(root,size)
    return size[0]/height


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    print("Density of given binary tree is ",
          density(root))
