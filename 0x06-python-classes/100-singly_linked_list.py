#!/usr/bin/python3
""" singly linked list"""


class Node:
    """" a node"""

    def __init__(self, data, next_node=None):
        """init node  instance variables"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ data attribute"""

        return (self.__data)

    @data.setter
    def data(self, value):
        """ attribute"""

        if not isinstance(value, int):
            raise TypeError('data will be an integer')
        self.__data = value

    @property
    def next_node(self):
        """get next_node attribute
        Returns: next node
        """

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ next node"""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node')

        self.__next_node = value


class SinglyLinkedList:
    """singly"""

    def __init__(self):
        """Init  singly """

        self.head = None

    def __str__(self):
        """list"""

        printsll = ""
        location = self.head
        while location:
            printsll += str(location.data) + "\n"
            location = location.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """insert
        Args:
            value: The value on the node
        """
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new
