from Node_Queue import NodeQ

class Queue:

    def __init__(self):
        self.__root = None


    def get_root(self):
        return self.__root

    def add_to_queue(self, node):
        if self.__root:
            node.set_next(self.__root)
        self.__root = node


    def print_queue(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()


    def remove_from_queue(self): #[node, marker, following_node]
        marker = self.__root

        if not marker.get_next():  #if marker is the only node in queue
            self.__root = None
            return marker

        while marker:
            following_node = marker.get_next()
            if following_node:
                if not following_node.get_next(): # We keep iterating until we get last node of queue. Then we make second last node as last node
                    marker.set_next(None)
                    return following_node.name
            marker = marker.get_next()


    def find_element(self, name):
        marker = self.__root
        while marker:
            if marker.name == name:
                marker.print_details()
                return
            marker = marker.get_next()
        raise TypeError("Name {} not found".format(name))


    def get_size(self):
        marker = self.__root
        count  = 0
        while marker:
            count += 1
            marker = marker.get_next()
        return count

