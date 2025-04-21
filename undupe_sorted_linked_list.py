# class node
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def undupe_sorted_linked_list(head):
    # visited set to store visited nodes 
    undupe_ls = [] 

    # init curr pointer
    curr = head

    # derive unique in visited set
    while curr is not None:
        if curr.val in undupe_ls:
           curr = curr.next
        else:
            # add curr to visited
            undupe_ls.append(curr.val)

            # update pointer forwards
            curr = curr.next

    # construct a new linked list
    new_node = tail = None
    for node in undupe_ls:
        # create new curr_node 
        curr_node = Node(node)

        # form new connections w/ existing
        # or new node
        if not new_node:
          new_node = curr_node 
          tail = new_node
        else:
           tail.next = curr_node
           tail = tail.next

    # return new_node
    return new_node 

if __name__ == "__main__":
    a = Node(4)
    b = Node(4)
    c = Node(6)
    d = Node(6)
    e = Node(6)
    f = Node(7)
    g = Node(7)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    # 4 -> 4 -> 6 -> 6 -> 6 -> 7 -> 7

    node = undupe_sorted_linked_list(a) # 4 -> 6 -> 7
    while node is not None:
        if node.next is None:
           print(node.val)
        else:
           print(node.val, end="->") 
        node = node.next