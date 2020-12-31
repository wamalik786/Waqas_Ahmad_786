#!/usr/bin/env python
# coding: utf-8

# In[75]:


import numpy as np


# In[3]:


x = np.arange(1,13).reshape((6,2))
print(x)


# In[9]:


x = np.arange(10,37, dtype = np.float64). reshape((3,3,3))
x


# In[81]:


a =np.arange(1,100*10+1).reshape((100,10))
x = a [(a % 7 == 0) & (a % 5 ==0)]
print(x)


# In[41]:


print("original matrix")
arr = np.arange(9).reshape(3,3)
print(arr)
print("swaped matrix")
arr[:,[0,1]] = arr[:,[1,0]]
arr


# In[44]:


z= np.zeros((4,5), dtype=int)
z


# In[82]:


arr = np.zeros(10, dtype=int)
print(arr)
print("\n Update fifth and eighth value")
arr[4] = 10
arr[7] = 20
print(arr)


# In[46]:


x = np.zeros(4, dtype=np.int64)
x


# In[58]:


x = np.full((2, 5), 6, dtype=np.uint32)
x


# In[60]:


a=np.arange(2,101,2)
print("\nArray of all the even integers from 2 to 100")
a


# In[85]:


arr = np.array([[3,3,3,],[4,4,4],[5,5,5]])
brr = np.array([1,2,3])
sub = arr[0]-brr[0],  arr[1]-brr[1], arr[2]-brr[2]
sub


# In[2]:


arr = np.array([0,1,2,3,4,5,6,7,8,9])  
arr[arr%2==1] = -1  
arr


# In[7]:


arr = np.array([1,2,3])
arr1 = np.repeat(arr,3)
ans = np.hstack((arr1,arr,arr,arr))
ans


# In[ ]:





# In[43]:


a = np.array([2,6,1,9,10,3,27])
print("Original array:")
print(a)
ind_pos = np.where(np.logical_and(a>5, a<10))
print("values in a range 5 to 10:")
arr[ind_pos]


# In[51]:


print("Creating 8X3 array using numpy.arange")
arr = np.arange(10,34,1)
arr = arr.reshape(8,3)
print (arr)

print("Dividing 8X3 array into 4 sub array\n")
ans = np.split(sampleArray, 4) 
print(ans)


# In[66]:


arr = np.array([[8,2,-2],[-4,1,7],[6,3,9]])
arr
ans = arr[np.argsort(arr[:,1])]
ans


# In[82]:


x = np.array([[1],[2],[3]])
y = np.array([[2],[3],[4]])
ans = np.dstack((x, y))
print (ans)


# In[111]:


arr = np.arange(1,10*10+1).reshape(10,10)
arr



# In[ ]:




