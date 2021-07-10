#!/usr/bin/env python
# coding: utf-8

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


# ## Udregninger med symboler

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


# ## Calculus i SymPy
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
