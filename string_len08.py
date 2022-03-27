def main(s):
    """
    Given variable type string s. Return the character in the muddle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    length = len(s)
    if length % 2 == 1:
        return s[length // 2]
    return s[length // 2 - 1: length // 2 + 1]


print(main('cool'))
