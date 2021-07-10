#!/usr/bin/env python
# coding: utf-8

# # Intro til pakker
# 
# Python er et af de mest brugte programmering sprog i verden specielt i den akademiske verden. Derfor er der også en kæmpe mængde pakker. Her i starten skal i stifte bekendskab med 4:
#  * Sympy
#  * Numpy
#  * Matplotlib
#  * Scipy
# 
# Det ligger næsten i navnet hvad de kan og hvad de skal bruges til:
#  * Sympy (Symbolic Python) er til symbolsk matematik
#  * Numpy (Numerical Python) er til numeriske beregninger
#  * Matplotlib (Mathematical ploting library) er til at lave plots 
#  * Scipy (Scientific Python) her skal vi kun bruge en funktion
# 
# Ligesom det er vigtigt at bruge den rigtige metode til at løse en ligning eller det rigtige værktøj til at slå et søm i er det også vigtigt at bruge den rigtige pakke til et programmerings problem. Gennerelt skal i bruge Sympy i LinAlys til at regne efter og lave simple plots så i kan tjekke jeres svar, Numpy og Matplotlib til at behandle og ilustrer jeres data fra laboratoriet og Scipy til at lave fits.
# 
# Der er også nogle overlap i pakkerne og de er også lavet til at kunne snakke sammen i skal dog så vidt som muligt undgå dette. Det kan skabe konflikter og give fejlder er svære at løse. 
# 

# ## Import 
# 
# For at hente en af de 4 ovenstående pakker ind i et python script skrives følgende:
# 

# In[13]:


import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as curve_fit


# Der er er 2 vigtige pointer. Man må aldrig bare importere alle pakkerne i starten uden at bruge dem alle og hvis man bruger dem alle kommer man nok i problemer så det skal du aldrig gøre. Det forvirrer dem der læsser jeres kode unødigt at du har pakker du ikke bruger. Dem der læsser din kode kan både være dine instruktore men også dig selv 3 måneder senere så gøre os og dig selv en tjenste og importer kun det du har brug for.
# 
# Derudover er der nogle uskrevende regler 'conventions' når man programmere så at alle skriver ens kode. Det gør at det er nemmer at læse for alle. En af dem er at man importere pakker med de samme navne brug derfor altid de navne der her er givet efter `as`.

# ## Hvordan bruger man en pakke?
# 
# Når man så har hentet sin pakke ind kan man kalde de funktioner som der er i den. For at gøre dette skriver man gennelerlt 
# `
# [forkortelse for pakke].[funktion]([variable])
# `
# fx `np.exp(2)` giver $e^2$. Her under ses nogle eksempler,

# In[14]:


# Både sympy og numpy har de kendte matematiske funktioner husk ikke at blande dem.
print(sp.cos(sp.pi)) 
print(np.cos(np.pi))


x = np.linspace(0,2*np.pi,1000)
y = np.cos(x)
plt.plot(x,y)


# Dette er det helt fundementale for hvordan pakker hentes og funktioner fra en pakke kaldes. Nu skal du så læsse de individuelle noter for at kunne bruge dem i dine studier.

# 

# In[ ]:




