from Functions import *

getday()
attendance()
free()

if day=='monday':
  submon()
elif day=='tuesday':
  subtue()
elif day=='wednesday':
  subwed()
elif day=='thursday':
  subthurs()
elif day=='friday':
  subfri()

for i, j in zip(freeclasses, subs):
  print(j[0], 'in', i)
