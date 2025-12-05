#looping backwards 
numbers = [1,2,3,4,5]
reversed = []
for i in range(len(numbers) -1,-1,-1):
   reversed.append(numbers[i]) 
 
print(reversed, 'reversed')

#looping backwards using slicing
rev = numbers[::-1]
print(rev, 'rev')

#looping backwards using recursion
def reverse_recursive(lst):
   if len(lst) <=1:
      return lst

   return [lst[-1]] + reverse_recursive(lst[:-1])

num = [10, 20, 30, 40]
rever = reverse_recursive(num)
print(rever, 'rev recur')
