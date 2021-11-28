# Program to find duplicate characters in String.
# input : programming
# output : r g m
def print_duplicate_characters(word):
    duplicates = {}
    for i in word:
        if i in duplicates:
            duplicates[i] += 1
        else:
            duplicates[i] = 1
    for key, value in duplicates.items():
        if value > 1:
            print(key, end=" ")


print_duplicate_characters("programming")
print_duplicate_characters("24tutorials")
