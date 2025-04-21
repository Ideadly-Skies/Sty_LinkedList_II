class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_cycle(head):
    curr = head
    visited = set()
    while curr is not None:
        if curr in visited:
          return True 
        
        # add curr to visited
        visited.add(curr)
        curr = curr.next
    
    return False

if __name__ == "__main__":
    q = Node('q')
    r = Node('r')
    s = Node('s')
    t = Node('t')
    u = Node('u')

    q.next = r
    r.next = s
    s.next = t
    t.next = u
    u.next = q # cycle

    #    ________________
    #  /                 \
    # q -> r -> s -> t -> u 

    print(linked_list_cycle(q))  # True

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d 

    print(linked_list_cycle(a))  # False