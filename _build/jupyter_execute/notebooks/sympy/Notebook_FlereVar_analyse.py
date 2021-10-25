#!/usr/bin/env python
# coding: utf-8

# # Analyse for funktioner af flere variable

# Vi har nu udvidet vores funktionsdefinition til at omfatte funktioner af flere variable. Som udgangspunkt kan vi bruge Python/SymPy på samme måde som for funktioner af en variabel. Til at starte med sørger vi for også at importerer variablen `y` fra `sympy.abc`, men vi kunne også tilføje flere variable og gennemføre tilsvarende beregninger for funktioner af 3 eller flere variable.

# In[1]:


import sympy as sp                    # Importer sympy
from sympy.abc import x, y            # Vi henter vores variabler


# For funktioner af flere variable bliver diffentialkvotienterne $f'$, $f''$ afløst af lidt flere begreber. Vi vil i det følgende demonstrere, hvordan man beregner partielt afledede, gradienter og Hesse-matricer (som dog først bliver berørt til sidst i LinAlys-kurset).
# 
# ## Partielt afledede
# Når vi går fra en til flere variable, spiller de partielt afledede en central rolle. De beregnes på en helt tilsvarende måde som vi tidligere har beregnet $f'$, idet vi blot skal være opmærksomme på, hvilken variabel, vi differentiere i forhold til. Vi har også ved differentiation af funktioner af en variabel (se notebook til uge 4) angivet navnet på den variable, f.eks. <code>sp.diff(expr, x)</code>, men dette var faktisk ikke strengt nødvendigt for simple funktioner, da SymPy i mange tilfælde kan gætte hvad der er den variable. Når vi har to variable, er det derimod afgørende at vi angiver den relevante variabel eksplicit.
# 
# Ellers foregår mange beregninger på samme måde:

# In[2]:


expr = sp.sin(x**2 * y)         # Vi definerer vores funktion af de to variable x og y
display(sp.diff(expr, x))       # Og differentierer, som vi plejer ift x
display(sp.diff(expr, y))       # Og i forhold til y


# Derimod giver <code>display(sp.diff(expr))</code> en fejlmeddelelse. Vi kan også differentiere flere gange efter hinanden i én kommando: Hvis vi f.eks. ønsker at udregne $\frac{\partial^2}{\partial x \partial y}\left ( x^2\cdot e^y\right )$, skriver vi <code>sp.diff(expr, y, x)</code>. 
# 
# Bemærk rækkefølgen af $x$ og $y$ her: i $\frac{\partial^2}{\partial x \partial y}$ står $\partial y$ bagerst, og logikken er, at da dette er nærmest funktionsudtrykket, skal vi differentiere efter $y$ først. Mere formelt er $\frac{\partial^2f}{\partial x \partial y} \equiv \frac{\partial}{\partial x}\left ( \frac{\partial f}{\partial y} \right )$. 
# 
# Når vi opskriver dette i Python, skal vi derimod liste variable i differentiations/integrationsrækkefølgen i almindelig læseretning. Dette giver os:

# In[3]:


expr = x**2*sp.exp(y)
display(expr,                  # Display kan bruges til at vise flere ting uden at kalde den flere gange.
        expr.diff(x),
        expr.diff(x, y),
        expr.diff(y),
        expr.diff(y, x))


# __Tip:__ For at gøre koden her mere læselig, nøjes vi med at kalde `display()` en gang, hvor vi til gengæld giver den flere udtryk som den skal vise. Desuden benytter vi, at `expr.diff(x)` er tilsvarende til `sp.diff(expr, x)`. 

# ## Gradienter og retningsafledede

# Et centralt begreb for funktioner af flere variable er gradienten, som vi (i funktioner af to variable) skriver som:  
# 
# $\nabla f(x,y) = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$
# 
# Vi tager altså den partielle differentieret i forhold til vores variable og sætter dem sammen som en vektor. 
# 
# Der er flere måder at beregne gradienten på i Python/SymPy, men her vil vi anvende en måde, der læner sig op af den måde, vi udregner den på i hånden. Vi vil altså lave en vektor bestående af de forskellige partielt afledede. Vi gør dette med <code>sp.derive_by_array()</code>, der som input skal bruge en funktion og en liste af de variable, der skal differentieres efter.
# 
# 
# Eksempel: Vi vil finde gradienten af $f(x,y) = e^{- x^2 - y^2}$.

# In[4]:


expr = sp.exp(- x ** 2 - y ** 2)

grad = sp.derive_by_array(expr, [x, y])
grad


# Resultatet kan umiddelbart aflæses, men hvis vi vil regne videre med gradienten som en vektor, bliver vi nødt til at benytte <code>sp.Matrix()</code> til at konvertere resultatet til matrixform, som vi kender fra [afsnittet om linær algebra](Notebook_LinAlg1.ipynb).
# 
# Lad os nu eksempelvis beregne den retningsafledede for ovenstående funktion i retningen $\left(\frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}}\right)$ i punktet med $(x, y) = (1, 2)$. Vi beregner nu jvf. TK sætning 2.57:

# In[5]:


grad_vec = sp.Matrix(grad)    # Konverterer til vektor/matrix-format
grad_vec                      # Vi viser det lige


# Vi definerer nu retningsvektoren med `sp.Matrix()`.

# In[6]:


retning = sp.Matrix([1/sp.sqrt(2), 1/sp.sqrt(2)])
retning


# Og nu kan vi beregne prikproduktet med `.dot()`: 

# In[7]:


prikket = grad_vec.dot(retning)
prikket


# Til sidst indsætter vi $(x, y) = (1, 2)$:

# In[8]:


resultat = prikket.subs(x, 1).subs(y, 2)
resultat


# ## Hessematricen
# Sidst i kurset vil vi bruge den såkaldte Hessematrix, der er en $n\times n$-matrix, der indeholder alle andenordens afledede for en funktion af $n$ variable. Vi vil specielt bruge determinanten af Hessematricen til at undersøge opførslen af funktioner af 2 variable omkring et stationært punkt (se TK sætning 3.4, der som det fremgår af kommentaren lige under sætningen kan formuleres ved hjælp af Hessematricen).
# 
# Man kunne beregne Hessematricen ved at beregne de dobbelt afledede som beskrevet ovenfor, men det er nemmere at importere den fra underbiblioteket af SymPy, som hedder <code>sympy.matrices</code>. Dette gøres med kommandoen <code>from sympy.matrices import hessian</code>. Herefter kan vi nu benytte <code>hessian(udtryk, variabelliste)</code> på samme måde, som vi brugte <code>sp.derive_by_array</code> til at udregne gradienten:

# In[2]:


from sympy.matrices import hessian        # Importer Hessematricen
expr = sp.exp(- x ** 2 - y ** 2)          # Definer samme funktion som tidligere

H = hessian(expr, [x, y])
display(H)


# Og hvis vi nu vil beregne værdien for $(x, y) = (0, 1)$, kan vi benytte <code>.subs()</code> to gange:

# In[3]:


H.subs(x, 0).subs(y, 1)


# In[ ]:




