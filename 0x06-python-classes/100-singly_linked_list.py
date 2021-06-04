#!/usr/bin/python3
"""Modulo Single_linked_list

this module define a class Node that store a number
and a class SinglyLinkedList that store the first element Node of the list

"""


class Node:
    """ Node of the a linked list """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ return the data """
        return self.__data

    @data.setter
    def data(self, value):
        """ set the data or raise a type error """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ return the next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ set the next node """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ save the head to the list, and adds elements on asc order """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """ insert a node with the value in the correct order """
        if type(value) != int:
            raise TypeError("data must be an integer")

        if self.__head is None or self.__head.data > value:
            self.__head = Node(value, self.__head)
        else:
            current_node = self.__head

            while (current_node.next_node is not None):
                if current_node.next_node.data > value:
                    break
                current_node = current_node.next_node

            current_node.next_node = Node(value, current_node.next_node)

    def __str__(self):
        current_node = self.__head
        list_as_str = ""
        separator = ""
        while (current_node is not None):
            list_as_str += (separator + str(current_node.data))
            separator = '\n'
            current_node = current_node.next_node

        return list_as_str
