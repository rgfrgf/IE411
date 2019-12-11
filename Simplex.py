#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


def simplex_step(A,b,c,iB,iN,xB,Binv,irule):
    #iBiN先需要sort排序
    CB=[]
    reduced_cost=[]
    for i in iB:
        CB.append(c[i])
    w=np.matmul(CB,Binv)
    for j in iN:
        reduced_cost.append(c[j]-np.matmul(w,A[:,j]))#negative to be the entering variable
    if optimal(reduced_cost)==1:
        istatus=-1
        return istatus,iB,iN,xB
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
            return istatus,iB,iN,xB
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
#        if y_k<=0:
#            index_nonpositive_r.append(r)
#        if y_k>0:
#            index_positive_r.append(r)
#    if len(index_nonpositive_r)==len(y_k):
#        istatus=16
#        return istatus,iB,iN,xB
#    else:
#        for i in range(len(index_positive_r)):
#            index_r=index_positive_r[i]
#            ratio.append(np.divide(xB[index_r],y_k[index_r]))
#        minimum_ratio=min(ratio)
        
        


# In[3]:


def negativereducedcost_bland(reduced_cost):
    ans=[]
    for k in range(len(reduced_cost)):#index of reduced cost
        if  reduced_cost[k]<0:
            ans.append(k)
        return min(ans)


# In[4]:


def negativereducedcost_smallest_coefficient(reduced_cost):
    return np.argsort(reduced_cost)[0]


# In[ ]:


def optimal(reduced_cost):
    for k in range(len(reduced_cost)):
        if reduced_cost[k]<0:
            return 0
        else:
            return 1


# In[53]:


#def update(Binv,k,r,y_k):
def update(k,r,y_k):
    E_inv=np.identity(len(y_k))
    vector=[]#-yik/ylk or 1/ylk column
    for i in range(E_inv.shape[0]):
        if i==r:
            vector.append(1/y_k[i])
        else:
            vector.append(-1*y_k[i]/y_k[r])        
    E_inv[:,k]=vector
    return E_inv
    #Binv_new=np.matmul(E_inv,Binv)


# In[ ]:


def pivot_bland(iB,iN,r,k):
    rout=r[0][0]#minimum index
    iBnew=iB.copy()
    index_in_iB=np.where(iB==r)
    iBnew[index_in]=k
    index_in_iN=np.where(iN==k)
    iNnew=iN.copy()
    iNnew[index_in_iN]=r
    return iBnew,iNnew


# In[56]:


y_k=np.array([1,2,1])
r=1
k=1


# In[57]:


update(k,r,y_k)


# In[7]:


CB


# In[9]:


#c=np.matrix('1;2;3')
#iB=np.matrix('0;1')

#CB=[]
#for  i in iB:
#    CB.append(c[i])

#A=np.array([[1,2,3],[3,4,5],[6,7,8]])
#A
#A[:,1]
#min(c)
#B=np.array([1,2,-5,-4,-9])
#B<0
#np.argsort(B[B<0])
#p=np.argsort(B[B<0])


# In[48]:


A=np.array([[1,2,3,4],[3,4,5,8],[6,7,8,9]])


# In[51]:


A[:,0]=np.array([9,9,9])


# In[52]:


A


# In[8]:





# In[40]:





# In[39]:





# In[36]:





# In[42]:


#np.argsort(B)


# In[52]:


#C=[1,2,3,4,6]


# In[55]:


#C[[1,3,5]]


# In[30]:


#ratio=np.array([-1,-3,11,8,8,8,9])


# In[33]:


#r=np.where(ratio==min(ratio[ratio>0]))


# In[ ]:





# In[34]:


#min(r)


# In[35]:


#r[0]


# In[36]:


#r[0][0]


# In[37]:


#r


# In[38]:


#r[0]


# In[41]:


#kk=r[0].copy()
#kk


# In[ ]:




