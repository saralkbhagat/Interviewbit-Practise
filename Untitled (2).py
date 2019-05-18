
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
    lis.append(x)
#     if len(x)<2:
#         del hashmap[sumarray[i]]
    


# In[15]:


s = []
for name in lis:
    if name not in s:
        s.append(name)


# In[16]:


s


# In[17]:


sindex=[]


# In[18]:


for item in s:
    try:
        
            maxx=item[-1]-item[0]
            sindex.append(maxx)
    except:sindex.append(0)


# In[19]:


sindex


# In[20]:


max(sindex)


# In[21]:


final=s[sindex.index(max(sindex))]


# In[22]:


start=final[0]


# In[23]:


end=final[-1]


# In[24]:


ret=inp[start:end]


# In[25]:


ret

