# Reverse words in a string
def reverseWords(s: str) -> str:
    end = len(s) - 1
    ans = ""
    for i in range(len(s) - 1, -1, -1):
        c = s[i]
        if c == " ":
            if i != end: ans += s[i + 1:end + 1] + " "
            end = i - 1
    if end >= 0:
        ans += s[:end + 1]
    else:
        ans = ans[:-1]
    return ans


print(reverseWords("the sky is blue"))
# print(reverseWords("  hello world  "))

def reverseWords2(s: str) -> str:
    return " ".join(s.strip().split()[::-1])