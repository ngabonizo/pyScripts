num = [1,2,3]
num.append(4)
print(num)

# utility function for append
def append(list, item):
  # this is how appending modifies the list in-place
  list[-1:] = [item]
  return list

append(num, 400)
print(num, 'number')
#this append util function actually deletes the last list value so its not a correct implementation of append()