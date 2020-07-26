
# coding: utf-8

# In[1]:


for i in range(5):
    for j in range(i+1):
        print("*",end =' ')
    print('')
for l in range (4,0,-1):
    for k in range(l):
        print("*",end =' ')
    print('')
    


# In[31]:


s = input('Enter the string ')
ls = len(s)
p =[s[i] for i in range(ls-1,-1,-1)]
k = ''.join(p)
print(k)


# In[27]:


for i in range(10, 2, -2):
    print(i, end=', ')

