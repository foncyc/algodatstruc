'''
Created on Aug 31, 2017

@author: Foncy
'''

class Node(object):
    
    def __init__(self, data):
        
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
    def insert(self, data):
        if data < self.data:
            if not self.leftChild:
                self.leftChild = Node(data)
            else:
                self.leftChild.insert(data)
        else:
            if not self.rightChild:
                self.rightChild = Node(data)
            else:
                self.rightChild.insert(data)
                
    def remove(self, data, parentNode):
        
        if data < self.data:
            
            if self.leftChild is not None:
                self.leftChild.remove(data, self)
                
            elif self.rightChild is not None:
                self.rightChild.remove(data, self)
                
            else:
                
                if self.leftChild is not None and self.rightChild is not None:
                    self.data = self.rightChild.getMin()
                    self.rightChild.remove(self.data, self)
                    
                elif parentNode.leftChild == self:
                    if self.lefthChild is not None:
                        tempNode = self.leftChild()
                    else:
                        tempNode = self.rightChild()
                    
                    parentNode.leftChild = tempNode
                    
                elif parentNode.rightChild == self:
                    if self.leftChild is not None:
                        tempNode = self.leftChild()
                    else:
                        tempNode = self.rightChild()
                    
                    parentNode.rightChild = tempNode
                    
    
    def getMin(self):
        if self.leftChild is None:
            return self.data
        else:
            self.leftChild.getMin()
    
    def getMax(self):
        if self.rightChild is None:
            return self.data
        else:
            self.rightChild.getMax()
            
    def traverseInOrder(self):        
        if self.leftChild is not None:
            self.leftChild.traverseInOrder()
        
        print(self.data)
        
        if self.rightChild is not None:
            self.rightChild.traverseInOrder()