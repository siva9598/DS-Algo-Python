class Node:
    def __init__(self,key):
        self.data =key
        self.left = None
        self.right = None


flag = [0]


def NthPostordernode(root, N):
    if (root == None):
        return

    if (flag[0] <= N[0]):

        # left recursion
        NthPostordernode(root.left, N)

        # right recursion
        NthPostordernode(root.right, N)

        flag[0] += 1

        # prints the n-th node of
        # preorder traversal
        if (flag[0] == N[0]):
            print(root.data)
root = Node(25)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(18)
root.left.right = Node(22)
root.right.left = Node(24)
root.right.right = Node(32)
N = [6]
NthPostordernode(root, N)
