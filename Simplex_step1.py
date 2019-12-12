#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd



def negativereducedcost_bland(reduced_cost):
    ans=[]
    for k in range(len(reduced_cost)):#index of reduced cost
        if  reduced_cost[k]<0:
            ans.append(k)
        return min(ans)




def negativereducedcost_smallest_coefficient(reduced_cost):
    return np.argsort(reduced_cost)[0]




def optimal(reduced_cost):
    for k in range(len(reduced_cost)):
        if reduced_cost[k]<0:
            return 0
        else:
            return 1





def update(Binv,k,r,y_k):
    E_inv=np.identity(len(y_k))
    vector=[]#-yik/ylk or 1/ylk column
    for i in range(E_inv.shape[0]):
        if i==r:
            vector.append(1/y_k[i])
        else:
            vector.append(-1*y_k[i]/y_k[r])        
    E_inv[:,k]=vector
    Binv_new=np.matmul(E_inv,Binv)
    return Binv_new



def pivot_bland(iB,iN,r,k):
    rout=r[0][0]#minimum index
    iBnew=iB.copy()
    index_in_iB=np.where(iB==r)
    iBnew[index_in]=k
    index_in_iN=np.where(iN==k)
    iNnew=iN.copy()
    iNnew[index_in_iN]=r
    return iBnew,iNnew




def pivot_smallest_coefficient(iB,iN,r,k):
    rout=r[0][0]#minimum index actually same with the one above
    iBnew=iB.copy()
    index_in_iB=np.where(iB==r)
    iBnew[index_in]=k
    index_in_iN=np.where(iN==k)
    iNnew=iN.copy()
    iNnew[index_in_iN]=r
    return iBnew,iNnew




def simplex_step(A,b,c,iB,iN,xB,Binv,irule):
    #iBiN先需要sort排序 index升序排列
    #sorting iB iN
    iB=np.sort(iB)
    iN=np.sort(iN)
    CB=[]
    reduced_cost=[]
    for i in iB:#Coefficient of Basic variables
        CB.append(c[i])
    w=np.matmul(CB,Binv)
    for j in iN:
        reduced_cost.append(c[j]-np.matmul(w,A[:,j]))#negative to be the entering variable
    if optimal(reduced_cost)==1:#get 1 if all reduced cost>=0
        istatus=-1
        return istatus,iB,iN,xB,Binv
    if irule==1:
        k=negativereducedcost_bland(reduced_cost)
    if irule==0:
        k=negativereducedcost_smallest_coefficient(reduced_cost)
    y_k=matmul(Binv,A[:,k])
    index_positive_r=[]
    index_nonpositive_r=[]
    ratio=[]#positive ratio set
    for r in range(len(y_k)):#ratio test
        ratio.append(np.divide(xB[r],y_k[r]))
        judge=np.where(len(ratio[ratio>0])>0,min(ratio[ratio>0]),-1)
        if judge==-1:
            istatus=16
            return istatus,iB,iN,xB,Binv
        else:
            r=np.where(ratio==judge)#r is a tuple, handle in the function pivot_bland/pivot_smallest_coefficient
            istatus=0
    if irule==1:
        iB_new,iN_new=pivot_bland(xB,r)
        Binv_new=update(B,k,r)
        xB_new=np.matmul(Binv_new,b)
    if irule==0:
        iB_new,iN_new=pivot_smallest_coefficient(xB,r,k)
        Binv_new=update(B,k,r,y_k)
        xB_new=np.matmul(Binv_new,b)
    return istatus,iB_new,iN_new,xB_new,Binv_new


