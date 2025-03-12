
def isPalindrom(s: str) -> bool:
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True


def longestPalindromeSubstring(s: str) -> str:
    res = ''

    for i in range(len(s)):
        st = s[i]
        for j in range(i+1, len(s)):
            res = st if isPalindrom(st) and len(st) > len(res) else res
            st = st+s[j]
            # res = max(res, len(st) if isPalindrom(st) else 0)
        res = st if isPalindrom(st) and len(st) > len(res) else res
    return res


# print(isPalindrom("chiihc"))

# input = 'a'
# input = 'abcs'
# input = 'csc'
# input = 'abbccccbba'

res = longestPalindromeSubstring(input)
print(res)