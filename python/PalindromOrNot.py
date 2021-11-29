# function to check string is
# palindrome or not
def isPalindrome(str):

    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

# main function
s = "malayalam"
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")




def isPalindrome(self, s: str) -> bool:
# Two pointer approach
        p1 = 0
        p2 = len(s)-1
        while (p1 <= p2): #O(N)
            # Move pointers to skip non-alphanumeric characters
            if (not s[p1].isalnum()):
                p1+=1
                continue
            if (not s[p2].isalnum()):
                p2-=1
                continue
            # compare & continue if matching
            if (s[p1].lower() == s[p2].lower()):
                p1+=1
                p2-=1
                continue
            else:
                return False
        return True