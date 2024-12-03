from Functions import *

day=input('Enter day: ')

if day=='monday':
  submon()
  attendance()
  free()
  for i, j in zip(freeclasses, subs):
    print(j[0], 'in', i)
elif day=='tuesday':
  subtue()
  attendance()
  free()
  for i, j in zip(freeclasses, subs):
    print(j[0], 'in', i)
elif day=='wednesday':
  subwed()
  attendance()
  free()
  for i, j in zip(freeclasses, subs):
    print(j[0], 'in', i)
elif day=='thursday':
  subthurs()
  attendance()
  free()
  for i, j in zip(freeclasses, subs):
    print(j[0], 'in', i)
elif day=='friday':
  subfri()
  attendance()
  free()
  for i, j in zip(freeclasses, subs):
    print(j[0], 'in', i)