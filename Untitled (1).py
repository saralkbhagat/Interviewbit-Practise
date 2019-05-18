
# coding: utf-8

# In[1]:


inp=[1 ,2 ,-2 ,4 ,-4]
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


hashmap={}
for i in range(len(inp)):
    hashmap[sumarray[i]]=[]


# In[9]:


for i in range(len(inp)):
    hashmap[sumarray[i]].append(i)
    


# In[10]:


hashmap


# In[11]:


lis=[]


# In[12]:


for i in range(len(inp)):
    x=hashmap[sumarray[i]]
    lis.append(x)
#     if len(x)<2:
#         del hashmap[sumarray[i]]
    


# In[13]:


s = []
for name in lis:
    if name not in s:
        s.append(name)


# In[14]:


s


# In[15]:


sindex=[]


# In[16]:


for item in s:
    try:
        
            maxx=item[-1]-item[0]
            sindex.append(maxx)
    except:sindex.append(0)


# In[17]:


sindex


# In[18]:


max(sindex)


# In[23]:


final=s[sindex.index(max(sindex))]


# In[28]:


start=final[0]+1


# In[27]:


end=final[-1]


# In[31]:


ret=inp[start:end+1]

