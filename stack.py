from Node_Stack import NodeS
from linked_list import LinkedList
from Node_LinkedList import Node


class Stack:

    def __init__(self):
        self.__linked_list = LinkedList()

    def push(self, node):
        self.__linked_list.add_to_list(node)

    def pop(self):
        return self.__linked_list.remove_start_from_list()

    def print_details(self):
        self.__linked_list.print_list()

    def get_size(self):
        return self.__linked_list.get_size()

