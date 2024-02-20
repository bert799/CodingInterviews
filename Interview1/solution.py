import string

def is_permutation_of_palindrome(phrase: str) -> bool:
    phrase = phrase.replace(' ', '').lower()
    phrase = phrase.translate(str.maketrans('', '', string.punctuation))
    odd_count = 0
    for char in set(phrase):
        if phrase.count(char) % 2 != 0:
            odd_count += 1
    return odd_count <= 1