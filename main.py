import random
#data generating functions
#base
def perm(n):
    temp = random.shuffle([i+1 for i in range(n)])
    return temp
def arr(n,mn,mx):
    temp = [random.randint(mn,mx) for i in range(n)]
    return temp
def pair(mn,mx):
    return(random.randint(mn,mx),random.randint(mn,mx))
#graph section
def tree(n):
    key = perm(n)
    temp = [random.randint(0,i) for i in range(n-1)]
    edges = []
    for i in range(len(temp)):
        edges.append((key[temp[i]],key[i+1]))
    random.shuffle(edges)
    return edges
def linegraph(n):
    edges = []
    key = perm(n)
    for i in range(n-1):
        edges.append((key[i],key[i+1]))
    return edges
def star(n):
    edges = []
    key = perm(n)
    for i in range(n-1):
        edges.append((key[0],key[i+1]))
    return edges
def binarytree(n):
    edges = []
    key = perm(n)
    for i in range(1,n):
        edges.append((key[(i-1)//2],key[i]))
    return edges
def graphgenerator(v,e):
    pass
#meta
def grid(code,m):
    temp = [exec(code) for i in range(m)]
    return temp
#driver functions

def makecase(randoms,edge,a):
    
    #random data section
    
    for i in range(randoms):
        f = open(str(i+1)+".in","w")
        
        #formatting area
        
        n = a[0]
        f.write(str(n)+'\n')
        for i in tree(a[0]):
            f.write(str(i[0])+" "+str(i[1])+'\n')
        n = a[1]
        f.write(str(n)+'\n')
        for i in tree(a[1]):
            f.write(str(i[0])+" "+str(i[1])+'\n')
            
        #end of formatting area
            
        f.close()
        
    #end of random data section
        
    #edge data section
        
    for i in range(edge):
        f = open(str(randoms+i+1)+".in","w")
        
        #formatting area
        
        n = a[0]
        f.write(str(n)+'\n')
        for i in linegraph(a[0]):
            f.write(str(i[0])+" "+str(i[1])+'\n')
            
        #end of formatting area
            
        f.close()
        
    #end of edge data section



from tkinter import *
import tkinter as tkin

def submit():
    global e1
    global e2
    makecase(int(e1.get()),0,list(map(int,e2.get().split())))
    e1.delete(0,"end")
    e2.delete(0,"end")
    
def find():
    global e3
    print(e3.get())
    try:
        f = open(e3.get(),'r')
        print(f.read())
    except:
        print("No such file!")
    e3.delete(0,"end")
    
def driver():
    global e1
    global e2
    global e3
    tk = Tk()
    tk.title("")
    l1 = Label(tk,text="Input number of test cases").grid(row=0,column=0)
    l2 = Label(tk,text="Input parameters").grid(row=1,column=0)
    e1 = Entry(tk)
    e1.grid(row=0,column=1)
    e2 = Entry(tk)
    e2.grid(row=1,column=1)
    b1 = Button(tk,text='Create!',bg='blue',fg='black',command=submit).grid(row=2,column=0)
    l3 = Label(tk,text="Browse testcase:").grid(row=3,column=0)
    e3 = Entry(tk)
    e3.grid(row=3,column=1)
    b2 = Button(tk,text='Show',bg='blue',fg='black',command=find).grid(row=4,column=0)
    tk.mainloop()
driver()
