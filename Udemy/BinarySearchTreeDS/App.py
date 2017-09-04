'''
Created on Aug 31, 2017

@author: Foncy
'''

from BinarySearchTreeDS.BinarySearchTree import BST

bst = BST()

bst.insert(12)
bst.insert(10)
bst.insert(-2)
bst.insert(1)
bst.traversInOrder()

print(bst.getMax())
print(bst.getMin())


bst.remove(-2)
bst.traversInOrder()

            
    
    
    
    
    
    
    
    
            
            
            
            
            
            
            