class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def middle_value(head):
    curr = head
    size = _find_length(_clone_list(head))
    for _ in range(size // 2):
       curr = curr.next
    return curr.val

# find length of linked list
def _find_length(curr):
    length = 0
    while curr is not None:
       curr = curr.next
       length += 1

    return length

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
    # a = Node('a')
    # b = Node('b')
    # c = Node('c')
    # d = Node('d')
    # e = Node('e')

    # a.next = b
    # b.next = c
    # c.next = d
    # d.next = e

    # a -> b -> c -> d -> e
    # print(middle_value(a)) # c

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # a -> b -> c -> d -> e -> f
    print(middle_value(a)) # d