import pytest
from itertools import combinations
from solution import Solution


l = [19, -50, 31, -10, 15, 23]
@pytest.mark.parametrize('target, expected_pair', [
    pytest.param(l[i] + l[j], (i, j), id=f'target={l[i]+l[j]}') for i, j in combinations(range(len(l)), 2)
])
def test_two_sum(target, expected_pair):
    i, j = expected_pair
    ret = tuple(Solution().twoSum(l, target))
    msg = f"Didn't work for input: {l}, {target}"
    assert (i, j) == ret or (j, i) == ret, msg