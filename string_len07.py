def main(s1, s2, s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    ans = "["
    if len(s1) % 2 == 1:
        ans += s1
    if len(s2) % 2 == 1:
        ans += f", {s2}"
    if len(s3) % 2 == 1:
        ans += f", {s3}"
    ans += "]"
    return ans


print(main(s1="codeschool.uz", s2="example", s3="python"))
