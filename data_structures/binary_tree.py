from Node_BinaryTree import NodeB

class BinaryTree:


    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root


    def add_element(self, node):
        if not self.__root:
            self.__root = node
        else:
            marker = self.__root
            while marker:
                if node.value == marker.value:
                    raise ValueError("Node with this value already exists")
                elif node.value > marker.value:
                    if not marker.get_right():
                        marker.set_right(node)
                        return
                    else:
                        marker = marker.get_right()
                elif node.value < marker.value:
                    if not marker.get_left():
                        marker.set_left(node)
                        return
                    else:
                        marker = marker.get_left()


    def find_element(self, value):
        marker = self.__root
        while marker:
            if marker.value == value:
                return marker.data
            elif marker.value < value:
                marker = marker.get_right()
            elif marker.value > value:
                marker = marker.get_left()
        raise LookupError("Element with value {} not found".format(value))


    def print_inorder(self):
        self.__print_inorder_r(self.__root)

    def __print_inorder_r(self, current_node):
        if not current_node:
            return
        self.__print_inorder_r(current_node.get_left())
        current_node.print_details()
        self.__print_inorder_r(current_node.get_right())



