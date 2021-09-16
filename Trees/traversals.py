class Node:
    def __init__(self,key):
        self.value =key
        self.left = None
        self.right = None

def printInorder(root):
    printInorder(root.left)
    print(root.value)
    printInorder(root.right)

def printPreorder(root):
    print(root.value)
    printPreorder(root.left)
    printPreorder(root.right)

def printPostorder(root):
    printPostorder(root.left)
    printPostorder(root.right)
    print(root.value)

def printInorderUsingStack(root):
    current = root
    stack = []
    while True:
        if (current is not None):
            stack.append(current)
            current = current.left
        elif (stack):
            current = stack.pop()
            print(current.value, end=" ")
            current = current.right
        else:
            break

def printLevelOrder(root):
    if root is None:
        return
    queue = []
    queue.append(root)

    while (len(queue) > 0):
        print(queue[0].value)
        node = queue.pop(0)
        if (node.left is not None):
            queue.append(node.left)
        if (node.right is not None):
            queue.append(node.right)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# printPreorder(root)
# printInorder(root)
# printPostorder(root)
# printInorderUsingStack(root)
printLevelOrder(root)
