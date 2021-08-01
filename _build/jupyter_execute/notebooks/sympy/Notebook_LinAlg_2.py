#!/usr/bin/env python
# coding: utf-8

# # Flere metoder i Linær Algebra
# Målet for denne sektion er at give en oversigt over de funktioner, som man kan få brug for, når man benytter SymPy som redskab i lineær algebra.
# 
# Langt de fleste funktioner i denne notebook virker på samme måde som matrixinversion, som for en matrix $A$ findes ved <code>A.inv()</code>.
# 
# Først importerer vi de rette pakker:

# In[1]:


import sympy as sp              # Importer sympy 
from sympy import Matrix        # Vi kommer til at lave mange matricer


# __Tip:__ Mange metoder i SymPy returnerer en liste over forskellige løsninger. Da disse ikke automatisk bliver vist som matematik, har vi mange steder sat en `*` foran metoden inde i `display`. I stedet for at skrive `display(*liste)` kan man i sin egen Notebook benytte sig af `sp.init_printing()` i starten af notebooken. Dette giver SymPy muligheden for at vælge, hvordan lister skal printes. Vi har desværre ikke kunne bruge denne mulighed på grund af formatteringen af vores notesbøger. 

# ## Transponering, adjungering og konjugering
# Hvis vi har givet en matrix, kan vi nemt beregne den transponerede matrix med at ombytte rækker og kolonner:

# In[2]:


A = Matrix([[1, 2], [3, 4]]);
display(A)


# Den transponerede beregnes med <code>.T</code>

# In[3]:


A.T    # Bemærk, at der ikke skal parenteser bag T


# Messer arbejder ikke med komplekse tal som indgange i matricer, men hvis man gør (og det er der mange gode grunde til, f.eks. i kvantemekanik), vil man også møde den såkaldte konjugerede matrix <code>A.conjugate()</code> (der fremkommer ved kompleks konjugering af indgangene af $A$) og den såkaldte adjungerede (matricen der er $A$s transponerede konjugerede matrix) <code>A.adjoint()</code> eller nemmere <code>A.H</code> . Notationen med H kommer af at den adjungerede matrix også kaldes den hermitisk konjugerede.
# Eksempelvis kan vi finde den konjugerede matrix her:

# In[4]:


from sympy import I, pi # Imaginære tal og pi skal hentes

A = Matrix([[1, 3+I], [2-I, sp.exp(I*pi/3)]])
display(A)
A.conjugate()


# hvor vi ser at alle imaginærdelene har skiftet fortegn.
# Som eksempel på den adjungerede (altså komplekst konjugerede og transponerede) matrix får vi

# In[5]:


A.H     # Som med .T indeholder syntaksen ikke ()


# ## Nulrum og søjlerum
# For en matrix $M$ kan vi finde dennes nulrum og søjlerum ved at bruge hhv. <code>M.nullspace()</code> og <code>M.columnspace()</code>. 

# In[6]:


M = Matrix([[1, 1, 2], [2, 1, 3], [3, 1, 4]])
display(M)
display(*M.nullspace())


# Hvilket giver en liste (her med eet element) af vektorer som er basis for matricens nulrum. Altså vektorer som opfylder ligningen $M\boldsymbol{x} = \boldsymbol{0}$. Dette gælder derfor også for linearkombinationer af vektorerne i nulrummet.
# 
# Søjlerummet findes helt tilsvarende:

# In[7]:


display(*M.columnspace())


# Herved får vi en liste af vektorer, som udspænder søjlerummet, og som består af de søjler fra $M$, der indeholder ledende indgange når $M$ er bragt på række-echelonform. Dette verificerer vi ved at betragte $M$s ækvivalente matrix på reduceret række-echelonform:

# In[8]:


display(*M.rref())


# ## Gram-Schmidt-ortogonalisering

# Er vi givet flere vektorer i rummet som ikke er lineært afhængigt af hinanden, kan vi danne et ortogonalt (og evt. ortonomalt, hvis vi normaliserer vektorerne) sæt af vektorer ved at bruge Gram-Schmidt-ortogonalisering. 
# 
# Dette kan være en ret omgangsrig procedure, som man i LinALys kun vil blive bedt om at udføre i relativt simple tilfælde. Men selv i disse simple tilfælde er der masser af muligheder for at lave regnefejl, og det kan derfor være rart hurtigt at kunne checke beregningerne, især for når der er tale om mere end 2-3 vektorer. Til dette importerer man <code>GramSchmidt</code> fra <code>sympy.matrices</code> og benytter den på en liste $L$ af vektorer: <code>GramScmidt(L)</code>. Som udgangspunkt normaliserer SymPy ikke de ortogonaliserede vektorer, men hvis vi giver funktionen et ekstra argument <code>GramSchmidt(L, True)</code>, fortages normaliseringen som en del af beregningen. 
# 
# Som eksempel genregner vi her eksemplet fra side 162 i Messer med SymPy:

# In[9]:


from sympy.matrices import GramSchmidt

# Definer en liste med matrix indgange, som nu er vektorer
L = [Matrix([1, 2, 2]), Matrix([0, 1, 0]), Matrix([0, 0, 1])]
display(*L)


# In[10]:


# Vi benytter nu GramScmidt
display(*GramSchmidt(L))


# In[11]:


# Eller hvis vi vil inkluderer en normalisering gør vi følgende:
display(*GramSchmidt(L, True))


# hvilket kan ses at passe med Messers 
# 
# $\left\{ \left(\frac{1}{3}, \frac{2}{3}, \frac{2}{3}\right), \left(\frac{-2}{\sqrt{45}}, \frac{5}{\sqrt{45}}, \frac{-4}{\sqrt{45}}\right),\left(\frac{-2}{\sqrt{5}}, 0, \frac{1}{\sqrt{5}}\right)\right\}$
# 
# ved anvendelse af kvadratrods- og brøkregneregler.

# ## Determinant
# Determinanten beregnes ved at tilføje <code>.det()</code> til matricens navn:

# In[12]:


A = Matrix([[1, 2], [3, 4]])
display(A)
A.det()


# Vi kan også beregne determinanten for en symbolsk matrix:

# In[13]:


from sympy.abc import a, b, c, d

B = Matrix([[a, b], [c, d]])
display(B)

B.det()


# i overensstemmelse med, hvordan vi selv ville regne den.

# ## Sporet / Trace
# Sporet udregnes ved at tilføje <code>.trace()</code> til den ønskede matrix, hvilket giver summen af diagonalindgangene:

# In[14]:


A = Matrix([[pi, 1, 1],[0, pi, 1],[0, 0, pi**2]])
display(A)
A.trace()


# ## Krydsprodukt, vektorprodukt / Cross product
# For to vektorer i tre dimensioner kan vi benytte beregne krydsproduktet mellem <code>v</code> og <code>w</code> med <code>v.cross(w)</code> (i analogi med hvordan vi beregner det indre produkt):

# In[15]:


v = Matrix([1, 0, 1])
w = Matrix([1, 2, 0])
display(v, w)

display(v.cross(w))

