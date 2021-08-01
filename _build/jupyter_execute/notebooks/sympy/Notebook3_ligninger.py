#!/usr/bin/env python
# coding: utf-8

# # Ligninger

# Første trin for at løse ligninger er at få skrevet ligninger op i et sprog, Python kan forstå. Det afgørende er her at indse at et lighedstegn kan have flere fundamentalt forskellige betydninger. Tidligere har vi tildelt variable bestemte værdier ved f.eks. at skrive <code>k = 4</code>, mens vi her vil bruge lighedstegnet til at beskrive et udsagn om sammenhængen mellem to udtryk. I SymPy-sprog er dette en _equality_ og syntaksen er (når vi har importeret SymPy som <code>sp</code> som vi plejer) givet ved <code>sp.Eq(venstre side, højre side)</code>. Pythagoras' læresætning kan f.eks. opskrives som:

# In[2]:


import sympy as sp
from sympy.abc import a, b, c             # Vi definerer a, b og c som symbolske variable

Pytha = sp.Eq(a ** 2 + b ** 2, c ** 2)    # Syntaks: sp.Eq(venstre side, højre side)
display(Pytha)


# Man kan ligeledes danne ligninger ved at sammensætte allerede definerede udtryk, her eksemplificeret ved cosinusrelationen:

# In[4]:


from sympy.abc import theta

expr = a**2 + b**2 - 2*a*b*sp.cos(theta) # Vi laver nu blot den ene side af ligningen som et udtryk (expr for "expression")
display(expr)

cos_relation = sp.Eq(c**2, expr)         # Og vi kan nu sammensætte højre- og venstresiderne
display(cos_relation)


# Vi kunne selvfølgelig også have gjort det hele i ét hug:

# In[8]:


cos_relation = sp.Eq(c**2, a**2 + b**2 - 2*a*b*sp.cos(theta))
display(cos_relation)


# Nu når vi har lighederne på plads, er det blevet tid til at lade SymPy regne for os. SymPy giver os to forskellige værktøjer til at løse ligninger, og det er lidt forskelligt, hvad de hver især er gode til. 

# ## Solveset
# Den første metode hedder solveset(), som kan oversættes til "løsningsmængde". Dette er den relativ ny metode, og SymPy-teamet arbejder på at denne skal være den primære løsningsmetode i fremtiden. Den løser dog ikke alle opgaver godt endnu, hvorfor vi nedenfor vil præsentere et alternativ.
# 
# Lad os prøve at løse en af overstående ligninger. Lad os tage helt standard Pythagoras $a^2 + b^2 = c^2$ (ligningen defineret som <code>Pytha</code> ovenfor). Hvis vi nu  kender $c=5$ og $a=3$ og ønsker at finde $b$, indsætter vi først værdierne i ligningen:

# In[9]:


display(Pytha)
Pytha_indsat = Pytha.subs([(a, 3), (c, 5)])
display(Pytha_indsat)


# Vi benytter nu solveset() til at løse denne. For en ligning virker denne funktion ved, at man angiver ligningen og den variabel, som man ønsker at løse for:

# In[10]:


solution = sp.solveset(Pytha_indsat, b)
display(solution)


# Vi har altså nu fundet løsningerne til ligningen. I tilfældet med Pythagoras' sætning leder vi efter en sidelængde, så vores løsning skal være et positivt tal. Vi kan indskrænke løsningsdomænet ved at give <code>solveset</code> et "domain"-keyword. Dette skal være et såkaldt _SymPy-set_, som er en lidt indviklet størrelse, men i langt de fleste tilfælde kan man slippe afsted med at bede om reelle tal ved at skrive <code>sp.Reals</code> eller ved at give et interval med <code>sp.Interval(_fra_, _til_)</code>, hvor man kan bruge <code>oo</code> for uendelig (forudsat at <code>oo</code> er blevet importeret). For mere avancerede løsningsdomæner henvises til dokumentationen [her](https://docs.sympy.org/latest/modules/sets.html). I dette tilfælde angiver vi et interval:

# In[11]:


from sympy import oo           # Vi importerer uendelig
pos_solution = sp.solveset(Pytha_indsat, b, sp.Interval(0, oo))
display(pos_solution)


# <code>solveset</code> virker også hvis vi istedet for en ligning angiver et udtryk (altså uden lighedstegn). Da sætter SymPy udtrykket lig med 0 og løser den derved fremkomne ligning (i dette eksempel $b^2-16 = 0$):

# In[12]:


pos_solution = sp.solveset(b**2 - 16, b, sp.Interval(0, oo))
display(pos_solution)


# Vi vil bruge den samme syntaks her, hvor vi vil finde rødder i et fjerdegrads polynomium. 

# In[13]:


from sympy.abc import x
expr = x ** 4 - 1
solutions = sp.solveset(expr, x) # Da vi har angivet et udtryk, sætter SymPy udtrykket lig med 0 og løser.
display(solutions)


# Er vi kun interesserede i reelle løsninger, kan vi indskrænke domænet til de reelle tal:

# In[14]:


solutions_real = sp.solveset(expr, x, sp.Reals)
display(solutions_real)


# Solveset virker også, hvis vi ikke har en numerisk værdi for alle symboler, men ønsker den generelle løsning. Hvis vi f.eks. vil finde $b$ i cosinusrelationen som defineret tidligere, kan vi skrive følgende:

# In[15]:


display(cos_relation)
sol_b = sp.solveset(cos_relation, b)
display(sol_b)


# Solveset() giver os løsninger skrevet op i mængdenotation for at give os de generelle fuldstændige løsninger. Selvom dette kan være meget fint i nogle tilfælde, ender vi dog i andre tilfælde med en generel og ganske ubrugelig løsning. Dette sker eksempelvis, hvis vi prøver at løse for $\theta$ direkte:

# In[16]:


sp.solveset(cos_relation, theta)


# Hvilket kan læses som "De værdier $\theta$ for hvilket det gælder at $\theta$ er et komplekst tal og at cosinusrelationen er opfyldt". Det er jo rigtig nok (sammenlign med selve cosinusrelationen!), men fortæller os ikke så meget, vi ikke vidste i forvejen. Det leder os videre til den anden metode til ligningsløsning:
# 
# ## Solve
# <code>Solve()</code> er den ældre funktion, som på trods af at være mindre generel oftest giver os en brugbar løsning. Syntaksen for input til <code>Solve()</code> er den samme som for <code>Solveset()</code>

# In[17]:


sp.solve(cos_relation, theta)


# Når der som her er flere løsninger, giver <code>Solve()</code>løsningerne som elementer i en liste, som <code>display</code> ikke kan konvertere til LaTeX. Vi må derfor nøjes med output i tekstformat eller vi kan bruge en løkke til at vise løsningerne en af gangen med `display`:

# In[23]:


sols = sp.solve(cos_relation, theta)
display(sols)           # Viser listen med løsninger som tekst ... OK, men ikke så kønt
for løsning in sols:    # Løkke, der viser løsningerne en af gangen med LaTeX-formattering
    display(løsning)


# Når man bruger <code>solve</code> kan man angive en liste af ligheder (eller uligheder), som afgrænser den variable. Hvis vi vil bestemme sidelængen $b$ (som er nul eller positiv) ved hjælp af Pythagoras' sætning, kan opgaven i solve-sprog lyde:

# In[24]:


display(Pytha_indsat)
sol_b = sp.solve([Pytha_indsat, b >= 0], b)
display(sol_b)


# Overordnet set er <code>solve</code> rigtig god til at give én løsning. Det kan altså ofte bruges i sammenhænge, hvor man vil tjekke et resultat, eller hvis man blot skal bruge en vilkårlig løsning og ikke den fuldstændige løsning.
# Eksempel: Vi løser $\sin(\theta) = 1$:

# In[26]:


sp.solve(sp.Eq(sp.sin(theta), 1), theta)


# Her får vi altså en løsning, og det vil ofte være den løsning, vi leder efter. Men da $\sin(x)$ er periodisk, ved vi, at der er flere løsninger. Så svaret er ikke udtømmende. 
# 
# I modsætning hertil har <code>solveset</code> den fordel, at den giver et  matematisk stringent svar, og den vil altså returnere hele løsningen:

# In[25]:


sp.solveset(sp.Eq(sp.sin(theta), 1), theta)


# ## Numerisk løsning
# Nogle gange kan vi komme ud for en situation, hvor en opgave ikke har en brugbar eksakt, symbolsk løsning, eller at hverken <code>solve</code> eller <code>solveset</code> giver et svar, vi kan bruge. Vi kan så benytte <code>sp.nsolve</code> til numerisk løsning af ligninger. Vi bruger således SymPy (som er designet til at være et symbolsk værktøj) til et formål, der er på kanten af dets anvendelsesområde, og vi skal derfor bruge værktøjet med forsigtighed. Det er derfor en god idé i disse tilfælde at tegne grafer for at illustrere opgaven. Derved kan vi checke at svaret rent faktisk giver mening i forhold til opgaven, og det tillader os også at give et ret godt gæt på en løsning.
# 
# Kaldesekvensen for at bestemme en numeriske løsning er:  
# ```python
# sp.nsolve(ligning, variabel, startgæt)
# ```

# Hvis nu vi eksempelvis vil finde en løsning til $x\log(x+1) = \sin(x)$, starter vi med at lave et plot (se notesbogen om plotning for en mere grundig forklaring af syntaksen).

# In[35]:


from sympy.abc import x
from sympy.plotting import plot

figur = plot(x * sp.log(x + 1), sp.sin(x), (x, 0, 2))


# Heraf ser vi altså, at et godt startgæt vil være omkring $x=1.2$. Dette vil vi nu bruge.

# In[38]:


lign = sp.Eq(x * sp.log(x + 1), sp.sin(x))
display(lign)
sp.nsolve(lign, x, 1.2)


# Sympy leder med `nsolve` blot efter en løsning. Vi kan altså ende med at få forskellige svar alt efter, hvad vores startgæt er. Gætter vi $x = 0.1$ får vi:

# In[39]:


sp.nsolve(lign, x, 0.1)


# som er en numerisk værdi meget tæt på 0, der også er en løsning til ligningen. Det er derfor vigtigt at være opmærksom på, hvilken løsning, der er relevant i en konkret sammenhæng, og lave et godt startgæt inspireret af dette.

# In[ ]:




