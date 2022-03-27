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
    l1 = len(s1) % 2
    l2 = len(s2) % 2
    l3 = len(s3) % 2
    if l1 + l2 + l3 == 0:
        return '[]'
    if l1 and l2 and l3:
        ans = f"[{s1}, {s2}, {s3}]"
    elif l1 and l2:
        ans = f"[{s1}, {s2}]"
    elif l1 and l3:
        ans = f"[{s1}, {s3}]"
    elif l2 and l3:
        ans = f"[{s2}, {s3}]"
    else:
        ans = f"[{s1 * l1}{s2 * l2}{s3 * l3}]"

    return ans


print(main(s1="codeschool.uz", s2="example", s3="python"))
