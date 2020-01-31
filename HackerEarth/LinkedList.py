# Implement linked list in python

class Node:

  element = None
  nextNode = None

  def __init__(self, element, nextNode):
    self.element = element
    self.nextNode = nextNode

  def getElement(self):
    return self.element

  def setNextNode(self, nextNode):
    self.nextNode = nextNode

  def getNextNode(self):
    return self.nextNode

class LinkedList:

  head = None
  tail = None
  count = 0

  # Initializes the LinkedList 
  def __init__(self, element):
    self.head = Node(element, None)
    self.tail = self.head
    self.count += 1

  # Prepends the element at the start of the list
  def prepend(self, element):
    newNode = Node(element, self.head)
    self.head = newNode
    self.count += 1
  
  # Appends the element at the end of the list
  def append(self, element):
    newNode = Node(element, None)
    self.tail.setNextNode(newNode)
    self.tail = newNode
    self.count += 1
  
  # Inserts the elements at the given position in the list
  def insertAt(self, position, element):
    
    if(position >= self.count):
      return self.append(element)
    
    previousNode = self.traverseTill(position - 1)

    newNode = Node(element, previousNode.getNextNode())
    previousNode.setNextNode(newNode)
    self.count += 1
  
   
  # Removes the element present at the given position
  def remove(self, position):
    previousNode = self.traverseTill(position - 1)
    nodeToBeRemoved = previousNode.getNextNode()
    if(nodeToBeRemoved == None):
      return
    previousNode.setNextNode(nodeToBeRemoved.getNextNode())
    self.count -= 1
   
  def reverse(self):

    if(self.count == 1):
      return self.head.getElement()
    
    previousNode = None
    current = self.head 
    while(current): 
        nextNode = current.getNextNode()
        current.setNextNode(previousNode) 
        previousNode = current 
        current = nextNode
    self.head = previousNode 

  
  def traverseTill(self, position):
    current = self.head
    currentPos = 0
    while(currentPos != position):
      current = current.getNextNode()
      currentPos +=1
    return current

  # Prints the list data
  def printList(self):
    node = self.head
    while node != None:
      print(node.getElement(), end = '->')
      node = node.getNextNode()
    print()
    

list = LinkedList(10)
print("First element")
list.printList()

list.prepend(5)
print("After prepend")
list.printList()

list.append(15)
print("After append")
list.printList()

list.insertAt(2, 12)
print("After insert at 2nd position")
list.printList()

print("Reversed element")
list.reverse()
list.printList()

list.remove(2)
print("After remove from")
list.printList()
