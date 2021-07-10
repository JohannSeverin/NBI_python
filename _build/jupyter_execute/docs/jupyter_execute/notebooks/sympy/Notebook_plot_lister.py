#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Eksempel-på-plot-af-række" data-toc-modified-id="Eksempel-på-plot-af-række-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Eksempel på plot af række</a></span></li></ul></div>

# # Hvordan plotter man?
# Kort note, består dog primært af eksempler på at plotte. 
# 
# Vi skal have eksempler på at plotte:
# - SymPY udtryk vha. sympy.plotting
# - Numerisk udtryks vha. math, matplotlib og for loops.

# ## Eksempel på plot af række

# In[1]:


# Vi importerer matplotlib.pyplot som bruges til at plotte med i Python
import matplotlib.pyplot as plt

# Vi importerer også numpy for at kunne regne med arrays
import numpy as np


# In[2]:


# Vi kan nu generere en række for at se, hvordan den udvikler sig:
# Vi starter med at definere et x_0
x_0 = 0.1
a = 1

# Vi laver nu en liste med de værdier vi vil have til sidst
x = x_0
værdier_1 = [x]

# Vi kan nu loope over 25 værdier og indsæt udtrykket i et udtryk
for i in range(15):         # Dette looper 25 gange
    x = 1/2 * (a + x)       # Vi definere x_n+1 = (x_n + a)/2
    print(x)                # Printer nuværende værdi
    værdier_1.append(x)       # Tilføjer nuværende værdi til vores liste


# In[3]:


plt.plot(værdier_1) # Hvis vi kun giver en liste bliver den blot plottet med indeks langs x aksen


# In[4]:


# Vi kan tilføje flere plots ved eksempelvis at ændre værdien for a:
# Vi kan nu generere en række for at se, hvordan den udvikler sig:
# Vi starter med at definere et x_0
x_0 = 0.1
a = 1.5

# Vi laver nu en liste med de værdier vi vil have til sidst
x = x_0
værdier_1_5 = [x]

# Vi kan nu loope over 25 værdier og indsæt udtrykket i et udtryk
for i in range(15):         # Dette looper 25 gange
    x = 1/2 * (a + x)       # Vi definere x_n+1 = (x_n + a)/2
    print(x)                # Printer nuværende værdi
    værdier_1_5.append(x)       # Tilføjer nuværende værdi til vores liste


# In[5]:


plt.plot(værdier_1)
plt.plot(værdier_1_5)


# In[ ]:




