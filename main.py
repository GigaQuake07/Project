from Functions import *

day=input('Enter day: ')
day=day.lower()
attendance()

if day=='monday':
  monday()
  for i, j in zip(freeclasses, subs):
    if j[-1][-1]!=i[-1][-1]:
      print(j[0], 'in', i[-1])
elif day=='tuesday':
  tuesday()
  for i, j in zip(freeclasses, subs):
    if i[-1][-1]!=j[-1][-1]:
      print(j[0], 'in', i[-1])
elif day=='wednesday':
  wednesday()
  for i, j in zip(freeclasses, subs):
    if i[-1][-1]!=j[-1][-1]:
      print(j[0], 'in', i[-1])
elif day=='thursday':
  thursday()
  for i, j in zip(freeclasses, subs):
    if i[-1][-1]!=j[-1][-1]:
      print(j[0], 'in', i[-1])
elif day=='friday':
  friday()
  for i, j in zip(freeclasses, subs):
    if i[-1][-1]!=j[-1][-1]:
      print(j[0], 'in', i[-1])