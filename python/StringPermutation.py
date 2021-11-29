# Find all permutation of a string

init_str = "abc"
result = []

def permutate(data, i, length):
    if i == length:
        result.append(''.join(data))
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            #print(data, i, length)
            permutate(data, i + 1, length)
            data[i], data[j] = data[j], data[i]


permutate(list(init_str),0,len(init_str))
print(result)


