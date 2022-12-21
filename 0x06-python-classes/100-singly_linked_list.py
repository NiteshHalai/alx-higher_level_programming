#!/usr/bin/python3
"""
This is a Nodes class
"""


class Node:

    """
    This is a Nodes class
    """
    
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @size.setter
    def data(self, value):
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @size.setter
    def next_node(self, value):
        self.__next_node = value


"""
This is a SinglyLinkedList class
"""


class SinglyLinkedList:

    """
    This is a SinglyLinkedList class
    """
    
    def __init__(self):
        self.__head

    def sorted_insert(self, value):

        # Special case for the empty linked list
        if self.__head is None:
            value.next = self.__head
            self.__head = value
 
        # Special case for head at end
        elif self.__head.data >= value.data:
            value.next = self.__head
            self.__head = value
 
        else :
 
            # Locate the node before the point of insertion
            current = self.__head
            while(current.__next_node is not None and
                 current.__next_node.__data < value.__data):
                current = current.__next_node
             
            value.__next_node = current.__next_node
            current.__next_node = value
