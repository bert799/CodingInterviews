class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

def check_final_nodes(head1: Node, head2: Node) -> tuple[bool, int, int]:
    len1 = 0
    len2 = 0
    while head1.next:
        len1 += 1
        head1 = head1.next
    while head2.next:
        len2 += 1
        head2 = head2.next
    return head1 == head2, len1, len2

def find_intersection(head1: Node, head2: Node) -> Node:
    if not head1 or not head2:
        return None
    is_intersecting, len1, len2 = check_final_nodes(head1, head2)
    if not is_intersecting:
        return None
    if len1 > len2:
        for _ in range(len1 - len2):
            head1 = head1.next
    else:
        for _ in range(len2 - len1):
            head2 = head2.next
    while head1 != head2:
        head1 = head1.next
        head2 = head2.next
    return head1


