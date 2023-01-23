def sum_largest(li):
  max = 0
  sec = 0
  for element in li:
    if element > max:
      element = max
      max = element
  return max + sec
def sumLargest(li):
  li.sort()
  return li[len(li - 1)] + li[len(li - 2]
def merge(li1, li2):
  li3 = []
  i = 0
  j = 0
  while i < len(li1) and j < len(li2)
    if li1(i)
    li3.append(element)
  return li3
def largestSoFar(li):
  count = 0;
  prev = float("-inf")
  for element in li:
    if element > prev:
      prev = element
      count += 1
  return count



def evens(li):
  count = 0
  for i in range(len(li)):
    if i % 2 == 0:
      if li[i] % 2 == 0:
        count += 1
  return count


li = [10, 8, 9, 9, 13, 16, 12]
print(evens(li))