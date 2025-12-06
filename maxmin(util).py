numbers = [10, 20, 5, 13 ,40 ,100, 15]

def min(list):
  minVal = list[-1]
  for value in list:
    if value < minVal:
      minVal = value
  return minVal
  
retVal = min(numbers)
print(retVal, 'min val')  


def max(list):
  maxVal = list[-1]
  for value in list:
    if value > maxVal:
      maxVal = value
  return maxVal

maxVal = max(numbers)
print(maxVal, 'maxval')        