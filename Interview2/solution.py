class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt
        
def find_intersection(head1: Node, head2: Node) -> Node:
    if not head1 or not head2:
        return None
    list1_set = set()
    while head1 is not None:
        list1_set.add(head1)
        head1 = head1.next
    while head2 is not None:
        if head2 in list1_set:
            return head2
        head2 = head2.next
    return None