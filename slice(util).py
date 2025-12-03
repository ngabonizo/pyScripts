number = [10, 20, 30]
number.insert(1, 100)
print(number, 'nubmer')

# insert() utility function *see the slicing implementation
def my_insert(list, index, item):
  list[index: index] = [item]
  return list

print(my_insert(number, 2, 200), 'insert util')