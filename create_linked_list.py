class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
    # init pointers 
    curr = tail = None

    for value in values:
        new_node = Node(value)

        if not curr:
           curr = new_node 
           tail = curr
        else:
           tail.next = new_node
           tail = tail.next

    # return curr in here
    return curr

if __name__ == "__main__":
    curr = create_linked_list(["h", "e", "y"]) # h -> e -> y
    while curr is not None:
        print(curr.val)
        curr = curr.next
