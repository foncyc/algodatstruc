'''
Created on Aug 30, 2017

@author: Foncy
'''

from LinkedListDS.LinkedList import LinkedList;
 
linkedList = LinkedList()

linkedList.insertStart(12)
linkedList.insertStart(3)
linkedList.insertStart(122)
linkedList.insertStart(122)
linkedList.insertStart(31)
linkedList.insertEnd(45)

linkedList.remove(122)

linkedList.traverseList()

print("LinkedList size: %d." % linkedList.size())
