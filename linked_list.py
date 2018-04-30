from Node_LinkedList import Node

class LinkedList:

    def __init__(self):
        self.__root = None


    def get_root(self):
        return self.__root


    def add_to_list(self, node):
        if self.__root:
            node.set_next(self.__root)
        self.__root = node


    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()


    def find_element(self, name):
        marker = self.__root
        while marker:
            if marker.name == name:
                marker.print_details()
                return
            marker = marker.get_next()
        raise LookupError("Student not found!")


    def remove_from_list(self, name):
        marker = self.__root

        if not marker.get_next():  # if marker is the only node in queue
            self.__root = None
            return marker

        while marker:
            following_node = marker.get_next()
            if following_node:
                if following_node.name == name:
                    if not following_node.get_next():
                        marker.set_next(None)
                        return following_node.name
                    else:
                        marker.set_next(following_node.get_next())
                        return following_node.name
            marker = marker.get_next()
        raise LookupError("Student {} not found".format(name))


    def remove_start_from_list(self):
        if not self.__root:
            raise RuntimeError("Tried to remove from the list but it was already empty!")
        removed_node = self.__root
        self.__root = self.__root.get_next()
        return removed_node


    def get_size(self):
        marker = self.__root
        count = 0
        while marker:
            count += 1
            marker = marker.get_next()
        return count

