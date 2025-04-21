class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_palindrome(head):
    # check if head is None
    if head is None:
       return True 
    
    # init pointers
    curr = head
    reversed_curr, count = _reverse_list(_clone_list(curr))

    for i in range(count // 2): 
       # not palindrome
       if curr.val != reversed_curr.val:
          return False

       # increment pointers fwd 
       curr = curr.next
       reversed_curr = reversed_curr.next

    return True

def _reverse_list(head):
  prev = None
  curr = head
  next = head.next
  count = 0

  while next is not None:
    curr.next = prev

    # update pointers
    prev = curr
    curr = next
    next = next.next
    count += 1

  # point curr to prev
  curr.next = prev
  count += 1

  # return new head
  return curr, count

# clone the linked list
def _clone_list(head):
    if not head:
        return None
    new_head = Node(head.val)
    current_old = head.next
    current_new = new_head
    while current_old:
        current_new.next = Node(current_old.val)
        current_new = current_new.next
        current_old = current_old.next
    return new_head

if __name__ == "__main__":
    a = Node(3)
    b = Node(2)
    c = Node(7)
    d = Node(7)
    e = Node(2)
    f = Node(3)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # curr, count = _reverse_list(a)

    # 3 -> 2 -> 7 -> 7 -> 2 -> 3
    print(linked_palindrome(a)) # True

    # while curr is not None:
    #    if curr.next is None:
    #     print("%d" %(curr.val))
    #    else:
    #     print("%d -> " %(curr.val), end="")
    #    curr = curr.next

    a = Node(3)
    b = Node(2)
    c = Node(4)

    a.next = b
    b.next = c

    # 3 -> 2 -> 4
    print(linked_palindrome(a)) # False