import math
# Project Euler problem 29. 

# initial values
list       = []
list_final = []
border     = 100
elements   = 0

for a in range(2, border+1, 1):
 for b in range(2, border+1, 1):
   list.append(float(math.pow(a,b)))

# Length of the list
length = len(list)

# removing double values
for i in range(0, length, 1): 
   j = i + 1
   while ( j < length): 
    if list[i] == list[j]:
      list[j] = 0
    j = j + 1
  
# Amount of distinct elements
for i in range(0, length, 1):
  if list[i] != 0:
     elements = elements + 1

print("Amount of distinct elements:", elements)
# Answer: 9183
