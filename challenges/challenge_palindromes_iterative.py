def is_palindrome_iterative(word):
    if word == "" or word != word[::-1]:
        return False
    return True
