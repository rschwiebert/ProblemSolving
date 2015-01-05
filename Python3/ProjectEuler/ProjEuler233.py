from math import *
filename='primesBelow1million.txt'
f=open(filename)
lines=f.readlines()
A=list()
B=list()

for line in lines:
    if int(line)%100000<100:
        print line
    if int(line)%4==1:
        
        A.append(int(line))
    elif int(line)%4==3:
        
        B.append(int(line))
    else:
        continue
        
def check(N):
    c=0
    L=int(ceil((1+2**.5)*N/2.0))
    for i in range(1,L):
        if (-4*N*i-4*i**2+N**2)>=0:
            if ((-4*N*i-4*i**2+N**2)**0.5)%1==0:
                #print i
                c+=1
    print 'For N=',N,'Number of points:',c
    
f.close()
storage=A[0:8]
C=list()
for a in storage:
    for b in storage:
        for c in storage:
            if a!=b and a!=c and b!=c and a**3*b**2*c<=10**11:
                C.append(a**3*b**2*c)
C.append(5**7*13**3)
C.append(5**10*13**2)

D=A[0:12500]
v=[i+1 for i in range(278454)]
for x in D:
    j=0
    while j*x<=278454:
        v[j*x-1]=0
        j+=1