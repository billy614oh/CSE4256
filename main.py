def matrix(m, n):
  li = []
  for i in range(m):
    li2 = []
    for j in range(n):
      li2.append((j + 1) + (n * i))
    li.append(li2)
  return li

def dot_product(li1, li2):
  sum = 0;
  for x in range(len(li1)):
    for y in range(len(li2)):
      if x == y:
        sum = sum + (li1[x] * li2[y])
  return sum


def identity(n):
  m = n;
  l = []
  for x in range(m):
    li2 = []
    for y in range(n):
      if x == y:
        li2.append(1)
      else:
        li2.append(0)
    l.append(li2)
  return l

def anti_diag(n):
  m = n;
  l = []
  for x in range(m):
    li2 = []
    for y in range(n):
      if y + x == m - 1:
        li2.append(1)
      else:
        li2.append(0)
    l.append(li2)
  return l
def transpose(m):
  l = []
  
  return l
  
print(transpose(5))


