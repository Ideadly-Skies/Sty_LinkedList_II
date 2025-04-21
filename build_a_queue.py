class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
    
  def enqueue(self, val):
    new_node = Node(val)
    if not self.head:
      self.head = new_node
      self.tail = self.head
    else:
      self.tail.next = new_node
      self.tail = self.tail.next
    self.size += 1

  def dequeue(self):
    if self.head is None:
      return "empty linked list!"

    # dequeue from the linked list 
    dequeue_val = self.head.val
    self.head = self.head.next
    self.size -= 1 
    return dequeue_val 