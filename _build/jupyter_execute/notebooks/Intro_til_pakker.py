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

# # Numpy
# Numpy er den pakke, som vi bruger til numeriske udregninger. Helt centralt er numpy arrays, som er lister, der tillader matematiske operationer på alle elementer samtidig. Vi starter med at importerer numpy:

# In[1]:


import numpy as np


# Og vi kan nu tage et liste af nogle tal og konverterer til et numpy array:

# In[3]:


array_af_tal = np.array([1, 4, 9, 16, 25])
array_af_tal


# Hvis vi nu benytter dette array i regne operation, foretages operationer på alle elementer af gangen:

# In[4]:


array_af_tal + 5 


# Derudover har numpy også en del indbygget matematiske operationer, som eksempelvis `cos`, `sin`, `sqrt` mm., som også kan bruges på enten et enkelt tal, eller på et helt array:

# In[5]:


np.sqrt(36)


# In[6]:


np.sqrt(array_af_tal)


# Yderligere benyttes numpy ofte til at regne statistik på et helt array, eksempelvis gennemsnittet af overstående array:

# In[7]:


np.mean(array_af_tal)


# En mere grundig gennemgang af numpy i MekRel sammenhænge se __link__.

# # Matplotlib Pyplot

# Matplotlib bruges til at plotte numeriske værdier fra eksempelvis laboratoriet. Vi importerer det ved:

# In[8]:


import matplotlib.pyplot as plt


# Herefter kan man nu benytte `plt.plot` til at plotte datapunkter: 

# In[13]:


x = np.array([1, 2, 3, 4, 5])
y = np.exp(x)

plt.plot(x, y, 'bo')
plt.title("Plot af punkter")
plt.xlabel("x")
plt.ylabel("y");


# Matplotlib kan desuden bruges til rigtig mange forskellige plot typer, og det er et super vigtigt værktøj i laboratoriet. Se hvordan det ellers bruges __link__. 

# # SymPy
# 
# Når vi skal foretage symbolske udregninger såsom at udregne grænser, foretage differentialregning eller løse ligninger benytter vi SymPy. 
# 
# Når vi benytter SymPy starter vi oftest med at gøre Python opmærksom på, at vi ikke har med numeriske værdier at gøre, men i stedet noget mere abstrakt, som altså ikke skal afrundes eller udregnes, men lige præcis behandles som et symbol.
# 
# For at starte op i SymPy importerer man biblioteket samt de symboler, som man gerne vil bruge fra ```sympy.abc```

# In[4]:


import sympy as sp                   # Importer biblioteket
from sympy.abc import x, a, b, phi   # Og de symboler som vi vil bruge. Vi kan altid hente flere   


# Når man nu benytter sympy kan blot kombinerer symbolerne til nye udtryk. Eksempelvis kan vi danne et udtryk  ved at gange og dividerer vores symboler med hinanden:

# In[5]:


a * b / x 


# Eller vi kan sammen sætte dette i nye udtryk, som vi nu kan behandle sammen:

# In[6]:


f = x * a * b
g = phi ** x 

display(f)
display(g)


# Her benytter vi ```display()``` i stedet for ```print()```, da vi ikke vil have en tekst version af vores symboler, men i stedet fortæller vi jupyter, at symbolerne skal skrives. Vi kan nu kombinere de to udtryk med hinanden:

# In[7]:


f * g ** (-f) - 1


# SymPy kommer nu også med en samling af funktioner, som vi kan bruge. Eksempelvis:

# In[8]:


display(sp.cos(x))                       # Udtryk med cosinus
display(sp.exp(f) ** 2 + sp.sqrt(g)** 2) # Udtryk med ekspoential funktioner og kvadratrødder 


# Der, hvor vi virkelig får glæde af SymPy er, når vi benytte det til differentiering, integration og til eksempelvis at finde grænser. Hvis vi nu har funktionen:   
# $ f(x) = \frac{x^2 - 4}{x + 2} \cdot e^{-x}$  
# 
# Kan vi benytte sympy til at finde grænser for $x \longrightarrow 2$

# In[16]:


from sympy.abc import x
f = (x ** 2 - 4)/(x + 2)* sp.exp(-x)
sp.limit(f, x, 2)


# Den afledte funktion:

# In[12]:


sp.diff(f, x)


# Eller til integration:

# In[17]:


from sympy.abc import a, b
sp.integrate(f, (x, a, b))


# For en nøjere gennemgang af SymPy og de mange andre muligheder, som det tilbyder, referer vi til **Indsæt link til SymPy Notebooks**
