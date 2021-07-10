#!/usr/bin/env python
# coding: utf-8

# <h1>Indholdsfortegnelse<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Almindelige-regneoperationer-med-komplekse-tal" data-toc-modified-id="Almindelige-regneoperationer-med-komplekse-tal-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Almindelige regneoperationer med komplekse tal</a></span></li><li><span><a href="#Komplekse-egenskaber" data-toc-modified-id="Komplekse-egenskaber-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Komplekse egenskaber</a></span><ul class="toc-item"><li><span><a href="#Modulus-og-argument" data-toc-modified-id="Modulus-og-argument-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Modulus og arguement</a></span></li><li><span><a href="#Kompleks-konjugering" data-toc-modified-id="Kompleks-konjugering-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Kompleks konjugering</a></span></li></ul></li><li><span><a href="#Rødder-og-ligninger" data-toc-modified-id="Rødder-og-ligninger-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Rødder og ligninger</a></span></li><li><span><a href="#Visualisering-af-det-komplekse-plan" data-toc-modified-id="Visualisering-af-det-komplekse-plan-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Visualisering af det komplekse plan</a></span></li></ul></div>

# # Komplekse tal i SymPy

# I LinALys lærer du at regne med komplekse tal. SymPy kan være en hjælp f.eks. til at visualisere alle løsninger til komplekse ligninger, men er i kurset primært et værktøj som du kan bruge til at checke de beregninger, der indgår i pointopgaverne og den afsluttende eksamen. Især hvis du har erfaring med at du laver mange regnefejl i omfattende beregninger, kan det være godt at checke beregningerne trin for trin i SymPy.
# 
# Vi starter med at importere den imaginære enhed ved hjælp af <code>from sympy import I</code>, $I$ er SymPys standardsyntaks for det imaginære tal $i$.

# In[2]:


import sympy as sp
from IPython.display import display
sp.init_printing()
from sympy import I, pi


# ## Almindelige regneoperationer med komplekse tal

# Når vi benytter <code>I</code>, får vi automatisk et komplekst tal, og SymPy behandler det som sådan ganske automatisk. Vi kan altså skrive $z = 3 + 4i$ som <code>z = 3 + 4 * I</code>:

# In[3]:


z = 3 + 4 * I
display(z)


# Eller vi kan lave et mere generelt udtryk, hvor vi istedet benytter symboler:

# In[4]:


from sympy.abc import a, b
w = a + b * I
display(w)


# Når vi først har defineret vores udtryk, så kan vi regne med dem på samme måde som med alle andre (reelle) tal. Regneoperationerne <code>+</code>, <code>-</code>, <code>*</code> og <code>/</code> fungerer som de skal.

# In[5]:


z = 1 + 2 * I
w = - 3 * I
display(z + w)


# In[6]:


display(z - w)


# In[7]:


display(z * w)


# Ved multiplikation og division er det nogle gange en god idé at bede SymPy om at reducere udtrykket. Især, hvis man gerne vil have det på en $x + yi$ form:

# In[8]:


sp.simplify(z * w)


# In[9]:


display(z / w)
display(sp.simplify(z / w))


# Man kan desuden beregne potenser af et kompleks tal på sædvandligvis ved at bruge <code>**</code>:

# In[10]:


z ** 3


# I dette tilfælde er der ikke meget hjælp at hente i <code>simplify</code>:

# In[11]:


sp.simplify(z ** 3)


# Vi kan til gengæld bede SymPy om at gange parentesen ud med <code>sp.expand</code>:

# In[12]:


sp.expand(z ** 3)


# SymPy ved hvordan den skal håndtere komplekse tal i mange sammenhænge, hvor fortolkningen er entydig. Man altså blot bruge komplekse tal i <code>sp.exp()</code>, <code>sp.cos()</code> eller lignende.

# ## Notationsformer og skift mellem disse

# ### Kartesiske koordinater, real og imaginærdel.
# 
# Funktionerne <code>sp.re()</code> og <code>sp.im()</code> giver real- og imaginærdelen af et komplekst tal. Det er naturligvis trivielt hvis vi starter med et imaginært tal af formen $x + iy$:

# In[13]:


z = 10 - 7 * I
display(z)
display(sp.re(z))
display(sp.im(z))


# Men det er mere oplysende, hvis vores komplekse tal har en anden form, for eksempel $4 e^{i \pi / 3}$:

# In[14]:


w = 4 * sp.exp(I * pi / 3)
display(w)
display(sp.re(w))
display(sp.im(w))


# ### Modulus og argument

# Vi kan desuden nemt beregne modulus og argument. Modulus for et komplekst tal er det samme som tallets absolutte værdi (TL s. 126) og findes med <code>sp.Abs()</code>. Bemærk at man bruger et stort A for at adskille kommandoen fra Pythons abs-funktion. For symbolske udtryk vil SymPy dog automatisk bruge sp.Abs() selv hvis vi bruger et lille a. Så for de to tal defineret ovenfor får vi:

# In[15]:


display(sp.Abs(z))
display(sp.Abs(w))


# Argumentet findes ved <code>sp.arg()</code> :

# In[16]:


display(sp.arg(z))
display(sp.arg(w))


# Hvorefter vi som nævnt tidligere kan bruge <code>.evalf()</code>, hvis vi vil have et bud på værdien af $-\arctan (7/10)$ med fire decimaler

# In[17]:


sp.arg(z).evalf(4)


# ### Kompleks konjugering

# Vi vil ret ofte benytte os af kompleks konjugering, hvor vi skifter fortegn på imaginærdelen (eller spejler i den reelle akse). Dette kan vi gøre ved brug af <code>sp.conjugate()</code>, som virker på imaginære tal uanset notationsform. Bemærk at funktionen hedder det samme som den tilsvarende funktion for matricer, som vi kender fra Lineær Algebra, men som har en anden syntax:

# In[18]:


display(z)
display(sp.conjugate(z))  # Konjugering af komplekst tal
display(z.conjugate())    # Konjugering af matrix ... men da z kan opfattes som en 1 x 1 matrix, er resultatet det samme


# In[19]:


display(w)
display(sp.conjugate(w))


# ## Rødder og ligninger

# En central egenskab ved de komplekse tal er, at et polynomium af n'te grad altid har netop n rødder (med multiplicitet). Vi skal ofte finde rødder i polynomier og løsninger til ligninger, og her indgår der ofte kvadratrødder og andre rødder af komplekse tal. Se TK 3.4.2 s. 141, hvor det fremgår at der altid er netop $n$ n'te rødder. Når vi vil finde den n'te rod af et komplekst tal, benytter vi <code>sp.root</code>. Syntaksen er således, at $\sqrt[n]{z}$ skrives som <code>sp.root(z, n, hvilken_rod)</code>, hvor <code>hvilken_rod</code> er et tal mellem $0$ til $n-1$ (husk at Python tæller fra 0) og fortæller SymPy, hvilken af de $n$ rødder, den skal udregne.

# In[20]:


z = - 3 + 3 * I
display(z)


# In[21]:


sp.root(z, 4, 0)


# Dette er utvivlsomt korrekt, men når man ønsker et mere anvendeligt svar, kan man f.eks. tvinge SymPy til at udregne real-delen og imaginærdelen som vi gjorde ovenfor:

# In[22]:


r1 = sp.root(z, 4, 0)
display(sp.re(r1))
display(sp.im(r1))


# Vi vil nu se på rødderne i et simplere tilfælde, nemlig $\sqrt[4]{-4}$.
# 
# Hvis vi ønsker at finde alle rødderne på en gang og få dem præsenteret i en liste, kan vi enten skrive det op som en ligning:

# In[23]:


from sympy.abc import x
sp.solve(sp.Eq(x**4, -4), x)


# Eller vi kan beregne rødderne en efter en ved hjælp af en for-løkke:

# In[24]:


for i in range(4):
    r = sp.root(-4, 4, i)
    display(sp.re(r) + I * sp.im(r))


# Vi kan finde rødder til polynomier ved hjælp af <code>sp.solve()</code>. Vi minder om at hvis vi kun giver <code>sp.solve()</code> et udtryk (og altså ikke en ligning, f.eks. dannet ved hjælp af <code>sp.Eq</code>), så finder funktionen løsninger til den ligning, der fremkommer når udtrykket sættes lig 0:

# In[25]:


from sympy.abc import z 
# Definer p som også har imaginære rødder
p =  z ** 3 - z ** 2 + 4 * z + -4

# Løs med sp.solve ved hjælp af udtrykket for p, der automatisk sættes lig nul
display(sp.solve(p))

# ... eller med en mindre elegant syntaks, hvor ligningen eksplicit er angivet til z3 - z^2 + 4z = 4
display(sp.solve(sp.Eq(z**3-z**2+4*z, 4), z))


# ## Visualisering i det komplekse plan

# Der er ikke et decideret tegneværktøj til komplekse tal i SymPy. Vi kan dog nå langt ved at lave udregningerne i SymPy og så tegne real- og imaginærdelene af tallet ved hjælp af _Matplotlib_. 

# Som eksempel vil vi prøve at visualisere hvad der sker, når vi tager et komplekst tal opløftet til en stigende potens. 

# In[32]:


import matplotlib.pyplot as plt

# Vi tager et eksempel med (1 + i/2)^n for n = 0, ..., 11
z = 1 + I/2

# Tom liste
zs = []
for i in range(12): # Vi kører nu igennem tolv gange (altså fra 0 til 11) og tilføjer potensen til en liste
    zs.append(sp.expand(z ** i))
    
display(zs)


# Vi viser her to mulige måder at visualisere disse tal på. Den første bruger SymPy, mens vi i den anden bruger NumPy til at lave en lidt nemmere numerisk løsning

# ### Visualisering i SymPy
# Først danner vi realdelene $x$ og imaginærdelene $y$, så tegner vi, og til sidst tilføjer vi linjer svarende til de reelle og imaginære akser. 

# In[47]:


xs = []
ys = []

for tal in zs:
    xs.append(sp.re(tal))
    ys.append(sp.im(tal))

plt.plot(xs, ys, "bx");

plt.hlines(0, -4, 4, ls = "--", color = "black");
plt.vlines(0, -3, 3, ls = "--", color = "black");


# Vi ser at værdierne starter i $z^0 = 1$ og spiralerer udaf idet $|z|>1$ og modulus af $z^n$ derfor vokser for stigende n. Argumentet vokser med en fast værdi hver gang $n$ vokser med 1.
# 
# ### Visualisering i NumPy
# Benytter vi i stedet NumPy, kan vi komme lidt lettere om ved det, og da SymPy alligevel konverterer til numeriske værdier inden graftegning, taber vi ikke det store. 

# In[35]:


import numpy as np

# Vi laver et numpy array, hvor vi specificerer datatypen til et numerisk-komplekst tal
zs = np.array(zs, dtype = complex);

# Så kan vi plotte det med at tage de reelle og imaginære værdier ud af arrayet direkt
plt.plot(zs.real, zs.imag, "kx");

# ... og linjer, der kan gøre det ud for akser
plt.hlines(0, -4, 4, ls = "--", color = "black");
plt.vlines(0, -3, 3, ls = "--", color = "black");


# Vi kan også bruge metoden til at vise rødderne i et polynomium.

# In[51]:


from sympy.abc import z

zs = sp.solve(z**3 + z**2 - 2)
display(zs)


# Her tegner vi ved hjælp af funktionen <code>scatter</code>, der giver mange grafiske muligheder for grafer bestående af enkelte "prikker", altså ikke-forbundne talpar.

# In[52]:


zs = np.array(zs, dtype = complex)
plt.scatter(zs.real, zs.imag, marker = "x", s = 20, color = "red")

# ... og linjer, der kan gøre det ud for akser. Længden er valgt således at inddelingerne på "akserne" er omtrent det samme.
plt.hlines(0, -2.7, 2.7, ls = "--", color = "black");
plt.vlines(0, -2, 2, ls = "--", color = "black");


# In[ ]:




