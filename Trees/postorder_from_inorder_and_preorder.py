def printPostOrder(In,Pre,n):
    root = In.index(Pre[0])

    if(root!=0): # if there are elements to the left of root in inorder
        printPostOrder(In,Pre[1:n],root)
    if(root!=n-1):
        printPostOrder(In[root+1:n],Pre[root+1:n],n-root-1)
    print(Pre[0],end = " ")


In = [4, 2, 5, 1, 3, 6]
Pre = [1, 2, 4, 5, 3, 6]
n = len(In)

print("Postorder traversal ")

printPostOrder(In, Pre, n)