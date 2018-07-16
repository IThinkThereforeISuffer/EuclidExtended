def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0
  q = []
  while a > 0 and b > 0:
    if a >= b:
      q.append(a//b)
      a = a % b
    else:
      q.append(b//a)
      b = b % a
  return max(a, b), q

def matricialProduct(a,b):
  result = [[0,0],[0,0]]
  for i in range(len(a)):
    for j in range(len(b[0])):
      for k in range(len(b)):
        result[i][j] += a[i][k] * b[k][j]
  return result
  
def diophantine(a, b, c):
  q, re = gcd(a,b)
  assert c % q == 0
  queues = []
  for i in range(len(re)):
    queues.append([[re[i],1],[1,0]])
  mat = [[1,0],[0,1]]
  for i in range(len(queues)):
    mat = matricialProduct(mat, queues[i]).copy()
  if len(re) % 2:
    signe = -1
  else:
    signe = 1
  p = c // q
  if a >=b:
    x = mat[1][1]
    y = -mat[0][1]
  else:
    y = mat[1][1]
    x = -mat[0][1]
  return signe*x*p, signe*y*p
def modularInverse(a, b, n):
  d,re = gcd(a, n)
  assert n > 1 and a > 0 and (d == 1)
  t,s = diophantine(n,a,1)
  x = b*(s % n) % n
  return x

def ChineseRemainderTheorem(n1, r1, n2, r2):
  (x, y) = ExtendedEuclid(n1, n2)

  n = (r2*x*n1  + r1*y*n2) % (n1*n2) 
  return  n

