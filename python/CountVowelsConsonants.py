# count a number of vowels and consonants in a given string

def count_vowels_consonants(s):
    s = s.lower()
    VowelsCount = 0
    ConsonantCount = 0
    for i in s:
        if str(i) in ("a","e","i","o","u"):
            VowelsCount = VowelsCount + 1
        elif str(i) >= 'a' and str(i) <= 'z':
            ConsonantCount = ConsonantCount + 1

    print("Vowels Count - ", VowelsCount)
    print("Consonant Count - ", ConsonantCount)

count_vowels_consonants("This is a really simple sentence")
