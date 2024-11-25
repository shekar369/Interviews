# Question : From list of numbers move Zero to the end of the list

list = [1,3,5,6,0,9,11,23,0,34,55,12,34,56]

# Solution
for item in list:
  if item == 0:
    list.remove(item)
    list.append(item)

print(list)

# output: [1, 3, 5, 6, 9, 11, 23, 34, 55, 12, 34, 56, 0, 0]
