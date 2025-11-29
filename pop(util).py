num = [1,2,3,4,5,6]
num.pop(1) # remove value at index=1
print(num)

#utility function
def my_pop(lst, index= -1):
  #handle negative index
  if index < 0:
    index += len(lst)

    #check for out-of-range index
    if index < 0 or index >= len(lst):
      raise IndexError('pop index out of range')
    
    #store the item to return
    item = lst[index]

    #Remove one element by slicing
    lst[index:index+1] = []

    return item
  
  my_pop(num, 3)
  print(num, 'num')