#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

display(data.head(10))


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.scatter(data['City'], data['Category'])

plt.title("Scatter plot")

plt.xlabel('City')
plt.ylabel('Category')

plt.show()


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.plot(data['City'])
plt.plot(data['Category'])

plt.title("Scatter plot")

plt.xlabel('City')
plt.ylabel('Category')

plt.show()


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.bar(data['City'], data['Category'])

plt.title("Bar Chart")

plt.xlabel('City')
plt.ylabel('Category')

plt.show()


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.hist(data['Category'])

plt.title("Histogram")

plt.show()


# In[27]:



import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter=";")

City = ['DKI Jakarta', 'Banten', 'Jawa Timur']
Quantity = [1, 2, 3]

plt.pie(Quantity, labels=City)
plt.title("Data Sales")
plt.show()


# In[28]:



import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter=";")

City = ['DKI Jakarta', 'Banten', 'Jawa Timur']
Quantity = [1, 2, 3]

plt.pie(Quantity, labels=City)
plt.title("Data Sales")
plt.savefig("pie.jpg")


# In[29]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.hist(data['Category'])

plt.title("Histogram")

plt.savefig("Histogram.jpg")


# In[30]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.bar(data['City'], data['Category'])

plt.title("Bar Chart")

plt.xlabel('City')
plt.ylabel('Category')

plt.savefig("bar chart.jpg")


# In[31]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.plot(data['City'])
plt.plot(data['Category'])

plt.title("Scatter plot")

plt.xlabel('City')
plt.ylabel('Category')

plt.savefig("scatter.jpg")


# In[32]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.scatter(data['City'], data['Category'])

plt.title("Scatter plot")

plt.xlabel('City')
plt.ylabel('Category')

plt.savefig("scatter plot.jpg")


# In[ ]:




