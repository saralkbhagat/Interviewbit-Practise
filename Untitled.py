
# coding: utf-8

# In[2]:


inp=[1 ,2 ,-2 ,4 ,-4]
outt=[2 ,-2 ,4 ,-4]


# In[6]:


sumarray=[i for i in range(len(inp)) ]


# In[7]:


sumarray=[None for i in range(len(inp)) ]


# In[8]:


sumarray


# In[10]:


for i in range (len(inp)):
    sum+=inp[i]
    sumarray[i]=sum


# In[9]:


sum=0


# In[11]:


sumarray


# In[70]:


hashmap={}
for i in range(len(inp)):
    hashmap[sumarray[i]]=[]


# In[71]:


for i in range(len(inp)):
    hashmap[sumarray[i]].append(i)
    


# In[72]:


hashmap


# In[80]:


lis=[]


# In[81]:


for i in range(len(inp)):
    x=hashmap[sumarray[i]]
    lis.append(x)
#     if len(x)<2:
#         del hashmap[sumarray[i]]
    


# In[85]:


s = []
for name in lis:
    if name not in s:
        s.append(name)


# In[86]:


s


# In[104]:


sindex=[]


# In[105]:


for item in s:
    try:
        
            maxx=item[-1]-item[0]
            sindex.append(maxx)
    except:sindex.append(0)


# In[106]:


sindex


# In[107]:


max(sindex)


# In[108]:


y=[4, 0, 0]


# In[109]:


max(y)

