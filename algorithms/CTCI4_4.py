class Node():
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def checkHeight(root):
    if not root:
        return -1

    leftHeight = checkHeight(root.left)
    if leftHeight == -1:
        return -1

    rightHeight = checkHeight(root.right)
    if rightHeight == -1:
        return -1

    diff = abs(leftHeight - rightHeight)

    if diff > 1:
        return -1
    else:
        return max(leftHeight,rightHeight)+1

def isBalanced(Node):

    return checkHeight(Node) != -1
