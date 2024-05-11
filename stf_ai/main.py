# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


"""
a,b,算出ab之间的最长的公共子串，返回，子串+长度
a = abab
b = bab
return bab
"""
def get_sub_common_str(s1,s2):
    n = len(s1) + 1
    m = len(s2) + 1
    res = ""
    dp = [[""] * n for _ in range(m)] # dp[i][j] 就表示以是s1[i-1],s2[j-1]
    for i in range(1,m):
        for j in range(1,n):
            if s1[j-1] == s2[i-1]:
                dp[i][j] = dp[i-1][j-1] + s1[j-1]
                res = max(res,dp[i][j],key = lambda x:len(x))
    return [res,len(res)]

a = "abcbcde"
b = "bbcbce"

print(get_sub_common_str(a,b))