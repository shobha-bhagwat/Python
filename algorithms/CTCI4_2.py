class Node():
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None

def getRootNode(arr):
    if not arr:
        return None

    mid = len(arr)//2

    root = Node(arr[mid])

    root.left = getRootNode(arr[:mid])
    root.right = getRootNode(arr[mid+1:])

    return root

def preOrder(Node):
    if not Node:
        return None

    print(Node.data)

    preOrder(Node.left)
    preOrder(Node.right)

arr = [3,5,7,9,10]
root = getRootNode(arr)
preOrder(root)



