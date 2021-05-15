class NodeQ:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.__next = None


    def set_next(self, node):
        if isinstance(node, NodeQ) or node is None:
            self.__next = node
        else:
            raise TypeError("The 'next' node must be of type node or None")


    def get_next(self):
        return self.__next

    def print_details(self):
        print("Name : {}  Phone : {}".format(self.name, self.phone))
