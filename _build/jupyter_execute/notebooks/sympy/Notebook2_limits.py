#!/usr/bin/env python
# coding: utf-8

# # Grænser
# En anden anvendelse af symbolske udtryk er beregning af grænseværdier. Fokus i kurset er på beregning af grænseværdier med papir og blyant, men det er godt at kunne checke sine resultater eller lave mere avancerede beregninger med SymPy. Dette gøres relativt nemt ved at benytte <code>sp.limit</code>-funktionen. Kaldesekvensen for funktionen er 
# <code>sp.limit(udtryk, variabel, grænse for variabel, retning)</code>. Efterlades retningen blank, beregnes grænseværdien oppefra / fra højre, og man får _ingen advarsel_ selvom grænseværdierne fra henholdsvis højre og venstre er forskellige.
# 
# Hvis vi nu eksempelvis vil beregne $\lim_{x\to 0} e^{-x}$ skriver vi:

# In[1]:


import sympy as sp            # Hent sympy 
from sympy.abc import x       # Vi vil bruge `x`
from sympy import oo          # Så kan vi tage grænserne i uendelig


# In[2]:


expr = sp.exp(-x)                    # Definer udtryk
display(sp.limit(expr, x, 0, '+'))   # Beregn og vis grænseværdien af udtrykket for x gående mod 0 oppefra ...
display(sp.limit(expr, x, 0, '-'))   # ... og nedenfra


# hvilket ikke er den store overraskelse, eftersom $e^{-x}$ er defineret i $x=0$, er kontinuert, og $e^0=1$.
# 
# Vi kan også beregne grænseværdier for $x\to\infty$:

# In[3]:


sp.limit(expr, x, oo)    # grænsen af udtrykket for x gående mod uendelig. Vi angiver ingen retning.


# Vær særligt opmærksom på situationer, hvor grænseværdien kunne være forskellig oppefra og nedefra, hvilket oftest forkommer for udtryk på brøkform i det/de $x$-værdier, hvor nævneren antager værdien nul. Betragt f.eks. $\displaystyle \frac{x^{4} + x^{2} + 1}{3 x^{3} - 19 x^{2} - x}$ når $x \to 0$:

# In[4]:


# Definer tæller og nævner hver for sig
poly1 = x ** 4 + x ** 2 + 1
poly2 = 3* x ** 3 - 19 * x **2  - x

# Kombiner dem til det ønskede udtryk og udskriv udtrykket til skærmen
poly_div = poly1 / poly2
display(poly_div)

# Tag grænsen af udtrykket, når x går mod 0 først oppefra / fra højre 
sp.limit(poly_div, x, 0, '+')


# In[5]:


# ... og dernæst nedefra / fra venstre:
sp.limit(poly_div, x, 0, '-')

