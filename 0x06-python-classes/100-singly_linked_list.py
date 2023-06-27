#!/usr/bin/python3

""" Implementation of a singly linked list in python

   Desc:
        - The list should be printable
        - You should be able to add nodes,
        in the linked list in sorted order.
"""


class Node:
    """ defines a node of a singly linked list.

        Attributes:
                   __data
                   __next_node
        properties:
                  data
                  next_node
    """

    def __init__(self, data: int, next_node=None):
        """ initialization of class Node

            Args:
               data: value for node
               next_node: value of the next node in list
        """
        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self) -> int:
        """ getter to get value of __data attribute
        """
        return self.__data

    @data.setter
    def data(self, value: int) -> None:
        """ setter to set new value for __data attribute

            Args:
                 value: new value for __data attribute
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ getter to get the value of __next_node attribute
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value: int):
        """ setter to set new value for __next_node attribute

            Args:
                 value: new value for __next_node attribute
        """
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ class that defines a singly linked list

        Attributes:
                   head: pointer to singly linked list
    """
    def __init__(self):
        """ initializing class instance

            Args:
                 head: pointer to singly linked list.
        """
        self.head = None

    def __repr__(self):
        """ format linked list values to string
        """
        values = []
        while self.head:
            values.append(str(self.head.data))
            if self.head.next_node:
                values.append("\n")
            self.head = self.head.next_node
        return "".join(values)

    def sorted_insert(self, value: int) -> None:
        """ insert new node to singly linked list

            Args:
                value: value of new node
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        # Special case for head at end
        elif self.head.data >= new_node.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            # Locate the node before the point of insertion
            current = self.head
            while current.next_node and current.next_node.data < new_node.data:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node
