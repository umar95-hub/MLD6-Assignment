
# coding: utf-8

# In[14]:


def my_reduce(fun,l):
    it = iter(l)
    m = next(it)
    for i in it:
        m = fun(i,m)
    return m


# In[19]:


def sum(a,b):
    return a+b


# In[20]:


my_reduce(sum,[6,8,9])


# In[24]:


def myfilter(func, iterable):
    it = iter(iterable)
    b=[]
    for value in it:
        if func(value) == True:
            b.append(value)
    return b


# In[25]:


myfilter(lambda x: x%2 == 0, [1,5,8,9])


# In[26]:


l2 = [ i*n for i in ['x','y','z'] for n in range(1,5) ]
l2


# In[27]:


l3 = [ i*n for n in range(1,5) for i in ['x','y','z'] ]
l3


# In[29]:


ln = [2,3,4]
l4 = [ [i+n] for i in ln for n in range(0,3)]
l4


# In[40]:


ln = [2,3,4,5]
l5= [[i+n for n in range (4)]for i in ln]
l5


# In[41]:


ln = [1,2,3]
l6 = [(n,i)for i in ln for n in ln]
l6

