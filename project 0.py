#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Connection to MongoDB instance
import pymongo
from pymongo import MongoClient


# In[2]:


# Estabilishing a connection
client = pymongo.MongoClient("localhost",27017)


# In[3]:


# Creating a database
database = client["Project_0"]


# In[4]:


# Creating a collection
collection = database["Meal Info"]


# In[5]:


# File data
docs = [{"meal_id":1885,"category":"Beverages","cuisine":"Thai"},{"meal_id":1993,"category":"Beverages","cuisine":"Thai"},{"meal_id":2539,"category":"Beverages","cuisine":"Thai"},{"meal_id":1248,"category":"Beverages","cuisine":"Indian"},{"meal_id":2631,"category":"Beverages","cuisine":"Indian"},{"meal_id":1311,"category":"Extras","cuisine":"Thai"},{"meal_id":1062,"category":"Beverages","cuisine":"Italian"},{"meal_id":1778,"category":"Beverages","cuisine":"Italian"},{"meal_id":1803,"category":"Extras","cuisine":"Thai"},{"meal_id":1198,"category":"Extras","cuisine":"Thai"},{"meal_id":2707,"category":"Beverages","cuisine":"Italian"},{"meal_id":1847,"category":"Soup","cuisine":"Thai"},{"meal_id":1438,"category":"Soup","cuisine":"Thai"},{"meal_id":2494,"category":"Soup","cuisine":"Thai"},{"meal_id":2760,"category":"Other Snacks","cuisine":"Thai"},{"meal_id":2490,"category":"Salad","cuisine":"Italian"},{"meal_id":1109,"category":"Rice Bowl","cuisine":"Indian"},{"meal_id":2290,"category":"Rice Bowl","cuisine":"Indian"},{"meal_id":1525,"category":"Other Snacks","cuisine":"Thai"},{"meal_id":2704,"category":"Other Snacks","cuisine":"Thai"},{"meal_id":1878,"category":"Starters","cuisine":"Thai"},{"meal_id":2640,"category":"Starters","cuisine":"Thai"},{"meal_id":2577,"category":"Starters","cuisine":"Thai"},{"meal_id":1754,"category":"Sandwich","cuisine":"Italian"},{"meal_id":1971,"category":"Sandwich","cuisine":"Italian"},{"meal_id":2306,"category":"Pasta","cuisine":"Italian"},{"meal_id":2139,"category":"Beverages","cuisine":"Indian"},{"meal_id":2826,"category":"Sandwich","cuisine":"Italian"},{"meal_id":2664,"category":"Salad","cuisine":"Italian"},{"meal_id":2569,"category":"Salad","cuisine":"Italian"},{"meal_id":1230,"category":"Beverages","cuisine":"Continental"},{"meal_id":1207,"category":"Beverages","cuisine":"Continental"},{"meal_id":2322,"category":"Beverages","cuisine":"Continental"},{"meal_id":2492,"category":"Desert","cuisine":"Indian"},{"meal_id":1216,"category":"Pasta","cuisine":"Italian"},{"meal_id":1727,"category":"Rice Bowl","cuisine":"Indian"},{"meal_id":1902,"category":"Biryani","cuisine":"Indian"},{"meal_id":1247,"category":"Biryani","cuisine":"Indian"},{"meal_id":2304,"category":"Desert","cuisine":"Indian"},{"meal_id":1543,"category":"Desert","cuisine":"Indian"},{"meal_id":1770,"category":"Biryani","cuisine":"Indian"},{"meal_id":2126,"category":"Pasta","cuisine":"Italian"},{"meal_id":1558,"category":"Pizza","cuisine":"Continental"},{"meal_id":2581,"category":"Pizza","cuisine":"Continental"},{"meal_id":1962,"category":"Pizza","cuisine":"Continental"},{"meal_id":1571,"category":"Fish","cuisine":"Continental"},{"meal_id":2956,"category":"Fish","cuisine":"Continental"},{"meal_id":2104,"category":"Fish","cuisine":"Continental"},{"meal_id":2444,"category":"Seafood","cuisine":"Continental"},{"meal_id":2867,"category":"Seafood","cuisine":"Continental"},{"meal_id":1445,"category":"Seafood","cuisine":"Continental"}]


# In[6]:


# Insert into meal info [insert_many]
result = collection.insert_many(docs)


# In[8]:


# Inserted_ids
inserted_ids_value = result.inserted_ids
print("Length: ",len(inserted_ids_value))

for i in inserted_ids_value:
    print(i)
    


# In[9]:


# Insert_one
var1 = {"meal_id":2,"category":"Snacks","cuisine":"Indian"}
res = collection.insert_one(var1)


# In[10]:


# Inserted -> id...not ids{for a single value}
value = res.inserted_id
value


# In[11]:


# Delete_one
collection.delete_one({'_id':1})


# In[12]:


# Delete many
collection.delete_many({})


# In[13]:


# To insert the elements again after deleting
collection.insert_many(docs)


# In[14]:


# Sort
[i for i in collection.find().sort("_id",-1)]


# In[15]:


result = collection.find().sort("_id",1)
for i in result:
    print(i)


# In[16]:


# Find
[i for i in collection.find()]


# In[17]:


# Find_one
collection.find_one({"category":"Salad"})


# In[18]:


# Update_many
var_2 = {'meal_id': 240, 'category': 'Snacks', 'cuisine': 'Italian'}
collection.update_many({"meal_id":24},{"$set":var_2})


# In[19]:


# Update_one
var_3 = {'meal_id': 249, 'category': 'Snacks', 'cuisine': 'Italian'}
collection.update_one({"meal_id":240},{"$set":var_3})


# In[20]:


# Limit
result_1 = collection.find().limit(24)
for i in result_1:
    print(i)


# In[ ]:





# In[ ]:




