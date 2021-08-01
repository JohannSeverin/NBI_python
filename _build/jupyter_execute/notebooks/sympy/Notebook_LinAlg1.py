#!/usr/bin/env python
# coding: utf-8

# # Vektorer og matricer

# I denne notebook vil vi have fokus på hvordan man definerer, manipulerer og foretager forskellige udregninger med matricer og vektorer. Som altid starter vi med at importere SymPy.

# In[1]:


import sympy as sp                    # Importer sympy


# Det grundlæggende er at definere matricer og vektorer på den nemmeste måde. Dette gøres ved at benytte den funktion, der hedder <code>Matrix()</code> fra SymPy. Da man oftest skal bruge denne mange gange, kan det være praktisk at importere den særskilt ved at skrive <code>from sympy import Matrix</code>, men det er lige så fint at skrive <code>sp.Matrix()</code>.
# 
# ## Vektorer - definition og regneoperationer
# Vektorer defineres ved at give en liste til Matrix funktionen. Vi kan altså skrive <code>Matrix([1, 1, 0])</code> for at få vektoren: 
# $\displaystyle \left[\begin{matrix}1\\1\\0\end{matrix}\right]$
# 
# 

# Vi kan angive de enkelte indgange som tal eller bruge symbolske variable som vi i forvejen har importeret fra `sympy.abc` ligesom vi tidligere har gjort med $x$. 
# 
# Eksempel:

# In[2]:


from sympy import Matrix
from sympy.abc import a, b, c

vektor1 = Matrix([a, b, c])
vektor1


# Det ligger os selvfølgelig også frit for at kombinere tal og variable:

# In[3]:


vektor2 = Matrix([a, sp.Rational(3, 4), b ** 2 / 2])   # Husk at bruge sp.Rational() til at definere brøker
vektor2


# De to vektorer <code>vektor</code> og <code>vektor2</code> kan nu kombineres på sædvanlig vis ved addition, subtraktion og skalarmultiplikation:

# In[4]:


vektor1 + vektor2   # Blot læg de to vektorer sammen med et almindeligt +


# In[5]:


a * vektor2       # a er importeret som et symbol, så vi kan bruge det som en skalar


# Hvis vi til gengæld forsøger at multiplicere de to vektorer får vi en fejl, da <code>*</code> mellem to Matrix-elementer er matrix-multiplikation, som ikke er defineret for to 3 x 1 matricer. Vi vender tilbage til matrixmultiplikation nedenfor, mens krydsprodukter kan findes i [sektionen om flere metoder i linæer algebra](Notebook_LinAlg_2.ipynb).
# 
# Et produkt, der derimod _er_ defineret for vektorer, er det fra gymnasiet velkendte skalarprodukt eller prikprodukt $\mathbf{v_1} \cdot \mathbf{v_2}$ som er et eksempel på et indre produkt (i Messers notation $\langle \mathbf{v_1}, \mathbf{v_2}\rangle$).
# 
# Et indre produkt mellem to vektorer <code>vektor1</code> og <code>vektor2</code> beregnes med <code>vektor1.dot(vektor2)</code>:

# In[6]:


vektor1.dot(vektor2)


# Som forventet får vi summen af produkterne af vektorens indgange, dog i en anden rækkefølge end vi normalt ville vælge ved udregning i hånden.

# ## Matricer - definition og regneoperationer

# Matricer defineres på samme måde, som vi har gjort det med vektorer, altså ved at benytte <code>Matrix()</code> - funktionen. Når vi laver en matrix, så skal vi dog give en liste af rækker, der hver især selv er lister. Formatet er det samme, som man bruger til at lave arrays i numpy. Hvis man eksempelvis blot vil lave en tabel med indgange fra 1 til 9, skal man angive det som:

# In[7]:


A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
display(A)


# Det er naturligvis en forudsætning, at alle rækkerne har lige mange elementer. 
# 
# Som for vektorer kan vi benytte symboler i matricer:

# In[8]:


B = Matrix([[a, b, c], [b, c, b], [c, b, a]])
display(B)


# Også addition og skalarmultiplikation fungerer som for vektorer:

# In[9]:


A + 3 * B


# In[10]:


42*B


# Matricer kan også multipliceres med hinanden (se Messer afsnit 5.1) så længe de har passende dimensioner. Man kan opfatte indgangen på plads (i,j) i produktet AB som prikproduktet af den i'te række i A med den j'te søjle i B, og for at dette kan lade sig gøre, skal antallet af søjler i A være det samme som antallet af rækker i B. Vi kan også skrive betingelsen som at hvis A er en matrix af dimension $m \times n$, skal B have dimension $n \times p$). I dette tilfælde kan vi gange dem sammen ved at benytte <code>*</code>:

# In[11]:


A * B


# Ligesom med arrays i numpy, kan vi også trække rækker/kolonner ud af matricer. Hvis vi vil have det øverste element til venstre i ovenstående matrix, kan vi gøre det ved:

# In[12]:


C = A * B
C[0, 0]


# Eller vi kan tage den tredje søjle ved:

# In[13]:


C[:, 2]


# ## Indbyggede matricer
# Til at definere en række meget almindeligt forekommende matricer er der indbygget smutveje.
# 
# Disse matricer skal importeres fra <code>sympy.matrices</code>.
# 
# __Identitetsmatricer:__ findes ved funktionen <code>eye(dimension)</code>. Navnet skyldes at "eye" udtales omtrent som "I", der ofte anvendes som symbol for identitetsmatricen, men allerede er reserveret til den imaginære enhed for komplekse tal. Da identitetsmatricen pr. definition er kvadratisk, angiver man blot dimensionen $n$ og får en $n\times n$ matrix med $1$ i diagonalen og $0$ alle andre steder:

# In[12]:


from sympy.matrices import eye

Id4 = eye(4)
display(Id4)


# __0- og 1-matricer:__ Funktionerne <code>zeros(dimension)</code> og <code>ones(dimension)</code> giver en matrix af den ønskede størrelse fyldt med hhv. 0 eller 1-taller. Her kan <code>dimension</code> være to tal <code>n, m</code> eller et enkelt tal <code>n</code>, hvilket resulterer i en $n \times n$ matrix:

# In[13]:


from sympy.matrices import zeros, ones

nul_matrix = zeros(4)
display(nul_matrix)


# In[14]:


fire_matrix = 4 * ones(3, 4)
display(fire_matrix)


# __Diagonalmatricer:__ laves med funktionen <code>diag(liste)</code>. Denne funktion giver man som input blot en liste med de ønskede diagonalelementer. Alle andre indgange er $0$:

# In[15]:


from sympy.matrices import diag

D = diag(1, 2, 3, 4)
display(D)


# Man kan også indsætte matricer langs diagonalen i større maricer, således at man får en blok-diagonal-matrix. Man kan f.eks. indsætte en matrix, der beskriver en rotation i planen, i en større matrix, der beskriver samme rotation i $(x,y)$-planen indlejret i et tredimensionalt rum:

# In[16]:


from sympy.abc import theta   # Importer theta

# Definer matrix
plan_rot = Matrix([[sp.cos(theta), sp.sin(-theta)], [sp.sin(theta), sp.cos(theta)]])
plan_rot


# In[17]:


# Lav diagonal med et 1-tal og så en matrice. diag fylder nu 0 ud alle andre steder.
rum_rot = diag(plan_rot, 1)
rum_rot


# Det er desuden muligt at sætte matricer sammen og definere matricer hvor hver indgang er resulatet af en beregning eller logisk test. [Disse metoder kan findes i dokumentationen her](https://docs.sympy.org/latest/modules/matrices/matrices.html) men vil ikke være nødvendige i LinALys-kurset.
