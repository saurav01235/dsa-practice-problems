# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.


def isMatch(s: str, p: str) -> bool:
    try:
        ind = 0
        _chr_buff = ''
        for chr in s:
            if p[ind] not in ['.', '*']:
                if chr != p[ind]:
                    return False
                else:
                    ind += 1
                    _chr_buff = chr
            else:
                if p[ind] == '.':
                    _chr_buff = chr
                    ind += 1
                elif p[ind] == '*':
                    if chr != _chr_buff:
                        return False
        return True
    except:
        print("--")
        return False






res = isMatch("ab", ".*")
print(res)


# res = isMatch("ab", ".*")
# print(res)