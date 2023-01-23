def evens(li):
  count = 0
  for i in range(len(li)):
    if i % 2 == 0:
      if li[i] % 2 == 0:
        count += 1
  return count

li = [10, 8, 9, 9, 13, 16, 12]

print(evens(li))