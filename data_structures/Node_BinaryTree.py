class NodeB:

    def __init__(self, value, data):
        self.data = data
        self.value = value
        self.__left = None
        self.__right = None


    def get_right(self):
        return self.__right

    def get_left(self):
        return self.__left

    def set_right(self, node):
        if isinstance(node, NodeB) or node is None:
            self.__right = node
        else:
            raise TypeError("The 'next' node must be of type node or None")


    def set_left(self, node):
        if isinstance(node, NodeB) or node is None:
            self.__left = node
        else:
            raise TypeError("The 'next' node must be of type node or None")


    def print_details(self):
        print("({},{})".format(self.value, self.data))
