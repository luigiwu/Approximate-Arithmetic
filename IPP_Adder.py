import math

def adder(A,B,a,b):
    c=int(not(a&b));
    C=int(not((A&(not B))|((not A)&B)));
    S=int(not(c&C));
    E=int(not(c|C));
    return S,E;

def add(A,B):
    S=[];
    E=[];
    for i in range(0,len(A)-1):
        s,e=adder(A[i],B[i],A[i+1],B[i+1]);
        S.append(s);
        E.append(e);
    S.append(int(A[len(A)-1] | B[len(B)-1]));
    E.append(0);
    return S,E;

def add_E(A,B):
    if len(A)>len(B):
        while len(A)!=len(B):
            B.insert(0,0);
    else:
        while len(A)!=len(B):
            A.insert(0,0);
    S=[];
    E=[];
    for i in range(0,len(A)-1):
        s,e=adder(A[i],B[i],A[i+1],B[i+1]);
        S.append(s);
        E.append(e);
    S.append(int(A[len(A)-1] | B[len(B)-1]));
    E.append(0);
    return S,E;



def norm_adder(a,b,c):
    tmp=int(not((a&(not b))|((not a)&b)));
    s=int(not((c&(not tmp))|((not c)&tmp)));
    c=int((a&b)or (a&c) or (b&c));
    return s,c;

def norm_add(A,B):
    if len(A)>len(B):
        while len(A)!=len(B):
            B.insert(0,0);
    else:
        while len(A)!=len(B):
            A.insert(0,0);
    sum=[];
    c=0;
    for i in range(0,len(A)):
        s,c=norm_adder(A[len(A)-1-i],B[len(A)-1-i],c);
        #print c;
        sum.insert(0,s);
    if c==1:
        sum.insert(0,1);
#print(sum);
    return sum;

'''
A=[1,0,1,0,1,1,1];
B=[0,0,1,1,0,1,0];
S,E=add(A,B);
print(E);
'''
'''
A=[1,0,1,0,1,1,1];
B=[0,0,1,1,0,1,0];
norm_add(A,B);
'''
