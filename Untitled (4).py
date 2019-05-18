
# coding: utf-8

# In[1]:


inp=[1, 2, -2, 4, -4]
outt=[2 ,-2 ,4 ,-4]


# In[2]:


sumarray=[None for i in range(len(inp)) ]


# In[3]:


sumarray


# In[4]:


sum=0


# In[5]:


for i in range (len(inp)):
    sum+=inp[i]
    sumarray[i]=sum


# In[6]:


sumarray


# In[7]:


sumarray.insert(0,0)


# In[8]:


sumarray


# In[9]:


hashmap={}
for i in range(len(inp)+1):
    hashmap[sumarray[i]]=[]


# In[10]:


for i in range(len(inp)+1):
    hashmap[sumarray[i]].append(i)
    


# In[11]:


hashmap


# In[12]:


lis=[]


# In[13]:


newmax=0


# In[14]:


for i in range(len(inp)+1):
    x=hashmap[sumarray[i]]
    
    if x not in lis and len(x)>1:
        localmax=x[-1]-x[0]
        if localmax>newmax:
            newmax=localmax
            lis.append(x)

    


# In[15]:


s=lis[-1]


# In[16]:


# sindex=[]


# In[17]:


# for item in s:
#     try:
        
#             maxx=item[-1]-item[0]
#             sindex.append(maxx)
#     except:sindex.append(0)


# In[18]:


# for item in s:
#     if item[-1]:
        
#             maxx=item[-1]-item[0]
#             sindex.append(maxx)
#     else:sindex.append(0)


# In[19]:


# sindex


# In[20]:


# final=s[sindex.index(max(sindex))]


# In[21]:


# start=final[0]


# In[22]:


# end=final[-1]


# In[23]:


ret=inp[s[0]:s[-1]]


# In[24]:


ret

