import mysql.connector as mc
from variables import *

def getday():
    global Day
    global day
    Day=input('Enter day: ')
    day=Day.lower()
    while day not in ['monday','tuesday','wednesday','thursday','friday']:
        Day=input('Enter day: ')
        day=Day.lower()

def attendance():
    global absent
    c = mc.connect(host='localhost', user='root', password='dpsbn@123', database='school')
    if c.is_connected():
        cur=c.cursor()
        q='SELECT TEACHER FROM TCHRSINFO'
        cur.execute(q)
        print('EmpNo', 'Teacher')
        for i in cur.fetchall():
            print(i)
            k=input('Present? ')
            if k in 'noNO':
                absent.append(i[0])
            else:
                continue
        c.close()
    else:
        print('Connection unsuccessful')

def free():
    global freeclasses
    global day
    c = mc.connect(host='localhost', user='root', password='dpsbn@123', database='school')
    if c.is_connected():
        cur=c.cursor()
        for i in absent:
            q='SELECT TEACHER, CLASSPERIOD FROM {}TT WHERE TEACHER="{}"'.format(day, i)
            cur.execute(q)
            for j in cur.fetchall():
                freeclasses.append(list(j))
        c.close()
    else:
        print('Connection unsuccessful')

def sub():
    global subs
    global day
    c = mc.connect(host='localhost', user='root', password='dpsbn@123', database='school')
    if c.is_connected():
        cur=c.cursor()
        for i, j in zip(freeclasses, absent):
            q='SELECT TEACHER, CLASSPERIOD FROM {}TT WHERE CLASSPERIOD NOT LIKE %s AND TEACHER!=%s'.format(day)
            cur.execute(q, (i[-1][-1], j))
            l=cur.fetchall()
            for k in l:
                print(k[0])
                #if k[0][0] not in absent and k[0][0] not in subs:
                 #  subs.append(k)

getday()
attendance()
free()
sub()

print(len(freeclasses))
print(subs)