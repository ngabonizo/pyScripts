num = [3,5,1,32,5]
num.remove(1) # remove() removes list item by it value on its first occurance
print(num)



def my_remove(list, value):
  for i in range(len(list)):
    if list[i] == value:
      list[i:i+1] = [] # remove by slice
      return
    
  raise ValueError("value not found in list")
  
numbers = [1,2,3,4,2]
my_remove(numbers, 3)
print(numbers, 'this are my numbers')

 