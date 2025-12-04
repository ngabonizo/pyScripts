# the range() utility function 

def my_range(stop):
  result = []
  i=0
  while i < stop:
    result.append(i)
    i+=1
  return result

print(my_range(5)) 


def range(start, stop=None, step=1):
  result = []

  if stop is None:
    stop = start
    start = 0

  if step == 0:
    raise ValueError('step cannot be zero') 
  
  i = start
  if step > 0:
    while i < stop:
      result.append(i)
      i += step

  else:
    while i > stop:
      result.append(i)
      i += step

  return result    

print(range(5))