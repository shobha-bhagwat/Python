class Node:
    # The linked list will store students' data

    def __init__(self, name, year, marks):
        self.name = name
        self.year = year
        self.marks = marks
        self.__next = None


    def set_next(self, node):
        if isinstance(node, Node) or node is None:
            self.__next = node
        else:
            raise TypeError("The 'next' node must be of type node or None")


    def get_next(self):
        return self.__next


    def print_details(self):
        print("{}: {} (year {})".format(self.name, self.marks, self.year))