import math
import TAM2


def int2list(a):
    A=[];
    for i in range(0,16):
        if a<2**(15-i):
            A.append(0);
        else:
            A.append(1);
            a=a-2**(15-i);
    return A;


def list2int(A):
    a=0;
    for i in range(0,len(A)):
        a=a+A[i]*(2**(len(A)-1-i));
    return a;

a=23455;
b=12335;
r=TAM2.mul(int2list(b),int2list(a));
print(list2int(r));


