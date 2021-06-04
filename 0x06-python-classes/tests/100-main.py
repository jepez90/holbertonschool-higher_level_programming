#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))

SinglyLinkedList = __import__('100-singly_linked_list').SinglyLinkedList

sll = SinglyLinkedList()
print(sll)
sll.sorted_insert(2)
print(sll)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
try:
    sll.sorted_insert("8")
except:
    sll.sorted_insert(8)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)
