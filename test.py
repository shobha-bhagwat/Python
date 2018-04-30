from Node_LinkedList import Node
from linked_list import LinkedList
from Node_Queue import NodeQ
from queue import Queue
from Node_Stack import NodeS
from stack import Stack
from Node_BinaryTree import NodeB
from binary_tree import BinaryTree




print("---------------------- Linked List -------------------------------")

name = "Mary"
marks = 54
year = 2

student = Node(name, year, marks)

linked_list = LinkedList()

linked_list.add_to_list(student)

linked_list.print_list()

names = ("John", 2, 99), ("Ron", 3, 68), ("Anna", 7, 81)

students = [Node(name, year, marks) for name, year, marks in names]

new_linked_list = LinkedList()

for student in students:
    new_linked_list.add_to_list(student)

new_linked_list.print_list()

new_linked_list.remove_from_list("Ron")

new_linked_list.print_list()

new_linked_list.find_element("Anna")



print("\n---------------------- Queue -------------------------------")

name = "Mary"
phone = "1-890-562"

person = NodeQ(name, phone)

queue = Queue()

queue.add_to_queue(person)

queue.print_queue()

persons = ("John", "1-675-657"), ("Ron", "1-908-089"), ("Anna", "1-987-987")

queue = [NodeQ(name, phone) for name, phone in persons]

new_queue = Queue()

for person in queue:
    new_queue.add_to_queue(person)

new_queue.print_queue()

print("Queue size is {}".format(new_queue.get_size()))

print("Removed element {} from Queue".format(new_queue.remove_from_queue()))

print("Queue size is {}".format(new_queue.get_size()))

#new_queue.find_element("John")

new_queue.find_element("Anna")



print("\n---------------------- Stack -------------------------------")

text = "Mary had a little lamb."

data = NodeS(text)

stack = Stack()

stack.push(data)

stack.print_details()

texts = ("Twinkle twinkle little star", "Johny Johny Yes Papa", "Fetch a pail of water")

paragraph = [NodeS(text) for text in texts]

new_stack = Stack()

for text in paragraph:
    new_stack.push(text)

new_stack.print_details()

print("Stack size is {}".format(new_stack.get_size()))

removed_element = new_stack.pop()

print("Removed element '{}' from Queue".format(removed_element.text))

print("Stack size is {}".format(new_stack.get_size()))


print("\n---------------------- Binary Tree -------------------------------")


tree = ((11, "A"), (13, "B"), (8, "C"), (12, "M"), (9, "N"), (5, "Y"), (10, "Z"))

nodes = [NodeB(value, data) for value, data in tree]

binarytree = BinaryTree()

for node in nodes:
    binarytree.add_element(node)

binarytree.print_inorder()

print(binarytree.find_element(8))


