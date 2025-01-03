# cách 1 
for x in range(1,51):
  if x % 2 == 0:
    print(x)
# cách 2
evens = [ print(x) for x in range(1,51) if  x%2 == 0]
