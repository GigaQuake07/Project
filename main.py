from Functions import *

day=input('Enter day: ')
day=day.upper()
attendance()
free()

if day=='monday':
  submon()
  for i, j in zip(freeclasses, subs):
    print(j[0], 'in', i)
elif day=='tuesday':
  subtue()
  for i, j in zip(freeclasses, subs):
    print(j[0], 'in', i)
elif day=='wednesday':
  subwed()
  for i, j in zip(freeclasses, subs):
    print(j[0], 'in', i)
elif day=='thursday':
  subthurs()
  for i, j in zip(freeclasses, subs):
    print(j[0], 'in', i)
elif day=='friday':
  subfri()
  for i, j in zip(freeclasses, subs):
    print(j[0], 'in', i)