


def get_core(dic_1,t):
    dic_2 = {}
    for item in t:
        dic_2[item] = dic_2.get(item,0) + 1
    for key in dic_2:
        if dic_1.get(key,0) < dic_2[key]:
            return False
    return True

def get_min_cover(s,t):
    start = 0
    end = 1
    dic_1 = {}
    dic_1[s[start]] = 1
    dic_1[s[end]] = dic_1.get(s[end],0) + 1
    res = s
    while end < len(s):
        if get_core(dic_1,t):
            res = min(res,s[start:end + 1],key=lambda x:len(x))
            dic_1[s[start]] -= 1
            if not dic_1[s[start]]:
                del  dic_1[s[start]]
            start += 1
        else:
            end += 1
            if end < len(s):
                dic_1[s[end]] = dic_1.get(s[end],0) + 1
    return res

print(get_min_cover(s = "ADOBECODEBANC", t = "ABCD"))
