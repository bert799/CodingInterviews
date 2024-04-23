from collections import deque
from solution import Solution


def stringify(node):
    if not node:
        return ''
    q = deque()
    q.append(node)
    rep = ''
    while q:
        node = q.popleft()
        l = node.left
        r = node.right
        rep += str(int(bool(l) + bool(r)))
        if l:
            q.append(l)
        if r:
            q.append(r)
    return rep


def _check(n, expected):
    ret = Solution().allPossibleFBT(n)
    tree_reps = set(stringify(root) for root in ret)
    assert len(tree_reps) == expected, f'Wrong answer for input {n}. Received: {len(tree_reps)}. Expected: {expected}.'


def test_1():
    _check(0, 0)


def test_2():
    _check(2, 0)
    _check(4, 0)
    _check(6, 0)
    _check(8, 0)
    _check(10, 0)


def test_3():
    _check(1, 1)


def test_4():
    _check(3, 1)


def test_5():
    _check(5, 2)


def test_6():
    _check(7, 5)


def test_7():
    _check(9, 14)


def test_8():
    _check(11, 42)


def test_9():
    _check(13, 132)


def test_10():
    _check(15, 429)


def test_11():
    _check(17, 1430)


def test_12():
    _check(19, 4862)
