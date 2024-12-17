import mysql.connector as mc
from variables import *

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

def monday():
    def monfree():
        global freeclasses
        global day
        c = mc.connect(host='localhost', user='root', password='dpsbn@123', database='school')
        if c.is_connected():
            cur=c.cursor()
            for i in absent:
                q='SELECT TEACHER, CLASSPERIOD FROM MONDAYTT WHERE TEACHER="{}"'.format(i)
                cur.execute(q)
                for j in cur.fetchall():
                    freeclasses.append(list(j))
            c.close()
        else:
            print('Connection unsuccessful')
    def submon():
        global subs
        global day
        c = mc.connect(host='localhost', user='root', password='dpsbn@123', database='school')
        if c.is_connected():
            cur=c.cursor()
            for i in absent:
                q='SELECT TEACHER, CLASSPERIOD FROM MONDAYTT WHERE TEACHER!=%s'
                cur.execute(q, (i,))
                l=cur.fetchall()
                for k in l:
                    subs.append(list(k))
    monfree()
    submon()

def tuesday():
    def tuefree():
        global freeclasses
        global day
        c = mc.connect(host='localhost', user='root', password='dpsbn@123', database='school')
        if c.is_connected():
            cur=c.cursor()
            for i in absent:
                q='SELECT TEACHER, CLASSPERIOD FROM TUESDAYTT WHERE TEACHER="{}"'.format(i)
                cur.execute(q)
                for j in cur.fetchall():
                    freeclasses.append(list(j))
            c.close()
        else:
            print('Connection unsuccessful')
    def subtue():
        global subs
        global day
        c = mc.connect(host='localhost', user='root', password='dpsbn@123', database='school')
        if c.is_connected():
            cur=c.cursor()
            for i in absent:
                q='SELECT TEACHER, CLASSPERIOD FROM TUESDAYTT WHERE TEACHER!=%s'
                cur.execute(q, (i,))
                l=cur.fetchall()
                for k in l:
                    subs.append(list(k))
    tuefree()
    subtue()

def wednesday():
    def wedfree():
        global freeclasses
        global day
        c = mc.connect(host='localhost', user='root', password='dpsbn@123', database='school')
        if c.is_connected():
            cur=c.cursor()
            for i in absent:
                q='SELECT TEACHER, CLASSPERIOD FROM WEDNESDAYTT WHERE TEACHER="{}"'.format(i)
                cur.execute(q)
                for j in cur.fetchall():
                    freeclasses.append(list(j))
            c.close()
        else:
            print('Connection unsuccessful')
    def subwed():
        global subs
        global day
        c = mc.connect(host='localhost', user='root', password='dpsbn@123', database='school')
        if c.is_connected():
            cur=c.cursor()
            for i in absent:
                q='SELECT TEACHER, CLASSPERIOD FROM WEDNESDAYTT WHERE TEACHER!=%s'
                cur.execute(q, (i,))
                l=cur.fetchall()
                for k in l:
                    subs.append(list(k))
    wedfree()
    subwed()

def thursday():
    def thursfree():
        global freeclasses
        global day
        c = mc.connect(host='localhost', user='root', password='dpsbn@123', database='school')
        if c.is_connected():
            cur=c.cursor()
            for i in absent:
                q='SELECT TEACHER, CLASSPERIOD FROM THURSDAYTT WHERE TEACHER="{}"'.format(i)
                cur.execute(q)
                for j in cur.fetchall():
                    freeclasses.append(list(j))
            c.close()
        else:
            print('Connection unsuccessful')
    def subthurs():
        global subs
        global day
        c = mc.connect(host='localhost', user='root', password='dpsbn@123', database='school')
        if c.is_connected():
            cur=c.cursor()
            for i in absent:
                q='SELECT TEACHER, CLASSPERIOD FROM THURSDAYTT WHERE TEACHER!=%s'
                cur.execute(q, (i,))
                l=cur.fetchall()
                for k in l:
                    subs.append(list(k))
    thursfree()
    subthurs()

def friday():
    def frifree():
        global freeclasses
        global day
        c = mc.connect(host='localhost', user='root', password='dpsbn@123', database='school')
        if c.is_connected():
            cur=c.cursor()
            for i in absent:
                q='SELECT TEACHER, CLASSPERIOD FROM FRIDAYTT WHERE TEACHER="{}"'.format(i)
                cur.execute(q)
                for j in cur.fetchall():
                    freeclasses.append(list(j))
            c.close()
        else:
            print('Connection unsuccessful')
    def subfri():
        global subs
        global day
        c = mc.connect(host='localhost', user='root', password='dpsbn@123', database='school')
        if c.is_connected():
            cur=c.cursor()
            for i in absent:
                q='SELECT TEACHER, CLASSPERIOD FROM FRIDAYTT WHERE TEACHER!=%s'
                cur.execute(q, (i,))
                l=cur.fetchall()
                for k in l:
                    subs.append(list(k))
    frifree()
    subfri()

