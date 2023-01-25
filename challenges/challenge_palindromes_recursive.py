def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    if word[0] != word[-1]:
        return False
    if word[0] == word[-1]:
        word = word[1:-1]
        if len(word) == 1 or len(word) == 0:
            return True
        low_index = word[0]
        high_index = word[-1]
        return is_palindrome_recursive(word, low_index, high_index)
