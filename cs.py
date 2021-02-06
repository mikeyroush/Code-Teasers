# given an array of ints, every element appears twice except one. 
# return the one element

given = [2,2,3,2]

# Hash solution, runtime O(n), works if other elements don't occur evenly
dict = {}

for num in given:
    dict[num] = dict[num] + 1 if num in dict else 1

for i, (key, val) in enumerate(dict.items()):
    if val == 1:
        print("Hash Result:", key)
        exit

# XOR solution, runtime O(n), only works if other elements occur evenly 
res = given[0]

for num in given[1:]:
    res = res ^ num

print("XOR Result: ", res)