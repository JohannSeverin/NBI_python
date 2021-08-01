#!/usr/bin/env python
# coding: utf-8

# # Egenværdier og -vektorer
# En central problemstilling i Linær algebra er at finde egenvædier og -vektorer af en matrice. Dette gøres relativt enkelt i SymPy.

# In[1]:


import sympy as sp
from sympy import Matrix


# For en matrix findes egenværdier og -vektorer med <code>A.eigenvals()</code> og <code>A.eigenvects()</code>.
# 
# <code>A.eigenvals()</code> giver os blot alle egenværdierne til en bestemt matrix i sorteret rækkefølge:

# In[2]:


A = Matrix([[2, 0, 0], [0, 3, 4], [0, 4, 9]])
display(A)


# In[3]:


A.eigenvals()


# Dette giver os nu en liste over egenværdierne (altså, 1, 2 og 11) og deres algebraiske multiplicitet, altså hvor mange gange den pågældende egenværdi er rod i det karakteristiske polynomium (her har alle egenværdierne algebraiske multiplicitet 1). For at illustrere hvordan resultaterne vises, "beregner" vi her egenværdierne for et trivielt eksempel:

# In[4]:


from sympy.matrices import eye
B = Matrix([[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 5]])
display(B)


# In[5]:


B.eigenvals()


# Funktionen <code>.eigenvects</code> virker på samme måde og giver både egenværdier og -vektorerne. Hvis man bruger `sp.init_printing()`, kan man kalde dette direkte ved blot at skrive `A.eigenvects()`. 

# In[6]:


A.eigenvects()


# Hvis vi vil vise resultatet i matematisk notation, er nogle krumspring nødvendige. Vi benytter `sp.latex()` til at konvertere det hele til LaTeX og viser derefter LaTeX-koden ved `display(Math())`.

# In[7]:


from IPython.display import Math
display(Math(sp.latex(A.eigenvects())))


# Her er resultatet altså givet som en liste med (egenværdi, multiplicitet, egenvektorer). Vi kan igen bruge det trivielle eksempel med B for at vise hvad der sker, når en egenværdi har flere tilhørende egenvektorer:

# In[8]:


display(Math(sp.latex(B.eigenvects())))


# I matematikkurser har matricerne gerne pæne (ofte heltallige) egenværdier, mens man i praksis sjældent oplever matricer med så velopdragne egenværdier. Dertil kommer, at store matricer kan gøre det meget hårdt for computeren at regne det hele symbolsk. Derfor vil man (når man eksempelvis beregner egenværdier i kvantemekanik) i stedet bruge NumPy, da der her er nogle ret hurtige implementeringer til at give gode numeriske løsninger. Heldigvis ligner metoderne meget hinanden, og hvis man skulle komme ud for at skulle løse et problem, der er for krævende med sumbolske beregninger, kan man finde NumPys LinAlg værktøjer [i den relevante dokumentation](https://numpy.org/doc/stable/reference/routines.linalg.html).

# ## Diagonalisering
# En afgørende pointe i kurset er at undersøge hvornår der kan findes en basis hvor en matrix $A$ er på diagonalform, altså hvornår der findes en matrix $P$, der opfylder at $D = P^{-1}AP$, hvor $D$ er en diagonalmatrix. For at finde $P$ og $D$ kan vi benytte <code>A.diagonalize()</code>. Vi regner videre med matricen <code>A</code> defineret ovenfor:

# In[9]:


display(A)


# In[10]:


display(*A.diagonalize())


# Outputtet for denne funktion er matricerne $P$ og $D$. Vi genkender at matricen $D$ netop indeholder egenværdierne langs diagonalen og at $P$ består at (multipla af) egenvektorerne. Vi kan få de pågældende matricer ud så vi kan regne videre med dem på følgende måde:

# In[11]:


(P, D) = A.diagonalize()
display(P, D)


# Og vi demonstrerer endelig at matricerne sammensættes som forventet. Først $D = P^{-1}AP$:

# In[12]:


P.inv() * A * P


# Eller omvendt $A = P D P^{-1}$

# In[13]:


P * D * P.inv()


# In[ ]:




