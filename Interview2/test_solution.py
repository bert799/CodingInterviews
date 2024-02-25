from solution import find_intersection


class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


def make_list(l: list) -> list[Node]:
    nodes = [Node(v) for v in l]
    for node, next in zip(nodes[:-1], nodes[1:]):
        node.next = next
    return nodes


def strlist(node: Node) -> str:
    s = []
    while node:
        s.append(str(node.value))
        node = node.next
    return '->'.join(s) or 'Empty'


def check(s1, s2, intersection):
    ans = find_intersection(s1, s2)
    msg = f"Didn't work for lists '{strlist(s1)}' and '{strlist(s2)}'"
    assert ans == intersection, msg


def check_both(s1, s2, intersection):
    check(s1, s2, intersection)
    check(s2, s1, intersection)


def test_example1():
    l1 = make_list([4, 7, 1, 9, 4, 5, 3])
    l2 = make_list([8, 2])
    l2[-1].next = l1[4]
    check_both(l1[0], l2[0], l1[4])


def test_example2():
    l1 = make_list([4, 7, 1, 9, 4, 5, 3])
    l2 = make_list([8, 2, 4, 5, 3])
    check_both(l1[0], l2[0], None)


def test_none():
    check_both(None, make_list([1, 2, 3, 4])[0], None)


def test_double_none():
    check_both(None, None, None)


def test_same_numbers():
    check_both(make_list(range(1, 10))[0], make_list(range(1, 10))[0], None)


def test_same_list():
    l = make_list(range(1, 10))
    check_both(l[0], l[0], l[0])


def test_in_last():
    l1 = make_list(range(1, 15))
    l2 = make_list(range(15, 25))
    last = Node(30)
    l1[-1].next = last
    l2[-1].next = last
    check_both(l1[0], l2[0], last)


def test_second():
    l = make_list(range(1, 15))
    n1 = Node(16, l[0])
    n2 = Node(16, l[0])
    check_both(n1, n2, l[0])


def test_one_empty():
    check_both(Node(1), None, None)


def test_one_one():
    check_both(Node(1), Node(1), None)
