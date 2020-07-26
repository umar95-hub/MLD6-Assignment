
# coding: utf-8

# In[2]:


n = list(range(2000,3201))
for i in n:
    if i%7==0 and i%5 !=0:
        print(i,end=",")


# In[3]:


fst = input("Please enter your first name- ")
snd = input("Please enter your last name- ")

print(snd,'',fst)


# In[1]:


d = int(input("input the Dia- "))
r = d/2
v = (4/3)*3.14*r**3
print("the volume of the spahereis ",v)

