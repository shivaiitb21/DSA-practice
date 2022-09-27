# create node
# create linked lists 
# add data to the linked lists  
# print linked lists 

from dataclasses import field


class Node:
    # Define init method that accepts the data we pass
    def __init__(self, data):
        self.data = data #data we receive as parameter   
        self.next = None #Initially next pointer points to nowhere initially -- assign it to none


class LinkedList():
    def __init__(self):
        self.head = None

    def insertHead(self, newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode

        del tempNode


    def listLength(self):
        currentNode = self.head
        length = 0

        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def insertAt(self, newNode, position):
        
        if position<0 or position>self.listLength():
            print("Invalid Position")
            return 

        if position == 0:
            self.insertHead(newNode)
            return

        currentNode = self.head
        currentPos = 0
        while True:
            if currentPos == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode    
            currentNode = currentNode.next
            currentPos += 1




    def insertEnd(self, newNode):
        #head => John, next of john points to None
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

# Node => data and next field
#create object for node class
#While creation of object pass the data field called name John
# Now firstNode.data => John  and firstNode.next => None
firstNode = Node(10) 
# Now add this node to linked list
linkedList = LinkedList()
#Linked list is intially empty >> head of linked list is none
#insert method in linked list to insert node into linked list
linkedList.insertEnd(firstNode)

secondNode = Node(20)
linkedList.insertEnd(secondNode)    

thirdNode = Node(15)
linkedList.insertAt(thirdNode, 25)


linkedList.printList() 