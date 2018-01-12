import math
import IPP_Adder as a


'''
A=[0,0,1,1,0,0,1,0,1];
B=[0,0,1,1];

print(a.add(A,B));
'''
def mul(A,B):
    S=[];
    E=[];
    for i in range(0,len(B)):
        if B[i]==0:
            S.append([0]*len(A));
        else:
            Z=[];
            for j in range(0,len(A)):
                Z.append(A[j]);
            S.append(Z);
        for j in range(0,len(B)-i-1):
            S[len(S)-1].append(0);
#print(S);
    size=len(S);
    S1=[];
    for i in range(0,size/2):
        S[2*i+1].insert(0,0);
        s=[];
        e=[];
        s,e=a.add(S[2*i],S[2*i+1]);
        S1.append(s);
        E.append(e);
#print(S1);
    size=len(S1);
    S2=[];
    for i in range(0,size/2):
        S1[2*i+1].insert(0,0);
        S1[2*i+1].insert(0,0);
        s=[];
        e=[];
        s,e=a.add(S1[2*i],S1[2*i+1]);
        S2.append(s);
        E.append(e);
#print(S2);
    size=len(S2);
    S3=[];
    for i in range(0,size/2):
        S2[2*i+1].insert(0,0);
        S2[2*i+1].insert(0,0);
        S2[2*i+1].insert(0,0);
        S2[2*i+1].insert(0,0);
        s=[];
        e=[];
        s,e=a.add(S2[2*i],S2[2*i+1]);
        S3.append(s);
        E.append(e);
#print(S3);
    size=len(S3);
    S4=[];
    for i in range(0,size/2):
        S3[2*i+1].insert(0,0);
        S3[2*i+1].insert(0,0);
        S3[2*i+1].insert(0,0);
        S3[2*i+1].insert(0,0);
        S3[2*i+1].insert(0,0);
        S3[2*i+1].insert(0,0);
        S3[2*i+1].insert(0,0);
        S3[2*i+1].insert(0,0);
        s=[];
        e=[];
        s,e=a.add(S3[2*i],S3[2*i+1]);
        S4.append(s);
        E.append(e);

    fe1=[];
    for i in range(0,len(E)/2+1):
        tmp=[];
        fe1,tmp=a.add_E(fe1,E[i]);
#print(fe1);
    fe2=[];
    for i in range(len(E)/2+1,len(E)):
        tmp=[];
        fe2,tmp=a.add_E(fe2,E[i]);
#print(fe2);
    error=[];
    for i in range(0,len(E)):
        tmp=[];
        error,tmp=a.add_E(error,E[i]);
#print(error);

    result=[];
    result=a.norm_add(S4[0],fe1);
    result=a.norm_add(result,fe2);
    #result=a.norm_add(result,error);
    return result;















'''
A=[1,1,1,1,1,0,1,0,0,0,1,1,0,0,1,0];
B=[1,0,1,1,0,0,1,0,0,0,1,1,0,0,1,0];
print mul(A,B);
print len(mul(A,B));
'''



