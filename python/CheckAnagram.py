# Program to Check if Two Strings are Anagram
# using set
def check_anagram(s1, s2):
    if set(s1.lower()) == set(s2.lower()):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


check_anagram('listen', 'silent')


# using sorted
def check_anagram2(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    # check if length is same
    if (len(s1) == len(s2)):

        # sort the strings
        sorted_str1 = sorted(s1)
        sorted_str2 = sorted(s2)

        # if sorted char arrays are same
        if (sorted_str1 == sorted_str2):
            print(s1 + " and " + s2 + " are anagram.")
        else:
            print(s1 + " and " + s2 + " are not anagram.")

    else:
        print(s1 + " and " + s2 + " are not anagram.")


check_anagram2('listen', 'silent')
