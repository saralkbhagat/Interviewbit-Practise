
# coding: utf-8

# In[1]:


inp=[ 1 ,2 ,-2 ,4 ,-4]
outt=[2 ,-2 ,4 ,-4]


# In[2]:


sumarray=[i for i in range(len(inp)) ]


# In[3]:


sumarray=[None for i in range(len(inp)) ]


# In[4]:


sumarray


# In[5]:


sum=0


# In[6]:


for i in range (len(inp)):
    sum+=inp[i]
    sumarray[i]=sum


# In[7]:


sumarray


# In[8]:


sumarray.insert(0,0)


# In[9]:


sumarray


# In[10]:


hashmap={}
for i in range(len(inp)+1):
    hashmap[sumarray[i]]=[]


# In[11]:


for i in range(len(inp)+1):
    hashmap[sumarray[i]].append(i)
    


# In[12]:


hashmap


# In[13]:


lis=[]


# In[14]:


for i in range(len(inp)+1):
    x=hashmap[sumarray[i]]
    if x not in lis:
        lis.append(x)

    


# In[15]:


s=lis


# In[16]:


sindex=[]


# In[17]:


for item in s:
    try:
        
            maxx=item[-1]-item[0]
            sindex.append(maxx)
    except:sindex.append(0)


# In[ ]:





# In[18]:


final=s[sindex.index(max(sindex))]


# In[19]:


start=final[0]


# In[20]:


end=final[-1]


# In[21]:


ret=inp[start:end]


# In[22]:




