from solution import is_permutation_of_palindrome


def _check(input_str, is_permutation):
    msg = f"Didn't work for string '{input_str}'"
    if is_permutation:
        assert is_permutation_of_palindrome(input_str), msg
    else:
        assert not is_permutation_of_palindrome(input_str), msg


def test_example():
    _check('Tact Coa', True)


def test_single_center():
    _check('naccnawaw', True)


def test_all_even():
    _check('anaccnawaw', True)


def test_some_upper():
    _check('ABCba', True)


def test_with_spaces():
    _check('abc c b a', True)


def test_with_punct():
    _check('abc!>b?...a', True)


def test_go_crazy():
    _check('?qs  Vq<a>> ds!*DV :o;Ao', True)


def test_not_example():
    _check('Tat Coa', False)


def test_not_single_center():
    _check('nacnawaw', False)


def test_not_all_even():
    _check('anacaccnawaw', False)


def test_not_some_upper():
    _check('ABCbBa', False)


def test_not_with_spaces():
    _check('acabc c b a', False)


def test_not_with_punct():
    _check('abbc!>b?...a', False)


def test_not_go_crazy():
    _check('?qsSV  Vq<a>> ds!*DV :o;Ao', False)
