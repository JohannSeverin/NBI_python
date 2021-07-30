#!/usr/bin/env python
# coding: utf-8

# # Intro til pakker
# 
# Python er et af de mest brugte programmeringsprog i verden, specielt i den akademiske verden. Derfor er der også en kæmpe mængde pakker, som kan løse alverdens problemer. Her i starten skal I stifte bekendskab med 4:
#  * Sympy ([dokumentation](https://www.sympy.org/en/index.html))
#  * Numpy ([dokumentation](https://numpy.org/doc/stable/))
#  * Matplotlib ([dokumentation](https://matplotlib.org/stable/index.html))
#  * Scipy ([dokumentation](https://docs.scipy.org/doc/scipy/reference/))
# 
# Det ligger næsten i navnet hvad de kan, og hvad de skal bruges til:
#  * Sympy (Symbolic Python) er til symbolsk matematik
#  * Numpy (Numerical Python) er til numeriske beregninger
#  * Matplotlib (Mathematical ploting library) er til at lave plots 
#  * Scipy (Scientific Python) her skal vi kun bruge en funktion
# 
# Ligesom det er vigtigt at bruge den rigtige metode til at løse en ligning, er det ligeså vigtigt at bruge den rigtige pakke til et programmeringsproblem. Som tommelfingerregel skal I bruge Sympy i LinAlys til at foretage symbolske udreginger for at kontrollere svar og lave nogle simple plots af funktioner. I laboratoriet skal I bruge Numpy og Matplotlib til at behandle og illustrere jeres data og Scipy til at lave fits.
# 
# Nogle af pakkerne har noget overlap, og de er lavet til at kunne bruges sammen. Til at starte med vil vi dog prøve at undgå dette, da det hurtig kan blive meget kompliceret og nok en kilde til fejl. 
# 

# ## Import 
# 
# For at hente en af de 4 ovenstående pakker ind i et python script benytter vi os af `import` nøgleordet, som fortæller python, at funktionerne skal hentes fra den pågældende pakke. Med `as` kan vi desuden give dem et andet (ofte kortere) navn, så man slipper for at skrive hele navnet hver gang man bruger pakken. Vi kan hente de fire pakker ved at skrive følgende i en celle: (i `scipy.optimize` specificerer vi her, at vi kun vil hente én funktion derfra, `curve_fit`) 
# 

# In[3]:


import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Selvom det er fristende altid at hente alle pakkerne, så er det en fordel kun at hente de pakker ind, som man skal bruge. Dette vil både gøre koden hurtigere, fordi Python ikke skal hente et stort bibliotek af funktioner, for at man kan bruge en enkel funktion. Det er også en fordel, hvis andre personer skal læse koden, at man tydeligt kan se, hvilke pakker og funktioner, som skal bruges for at køre ens kode.  

# Nogle pakker bruger vi så ofte, at vi gerne forkorter deres navne, så vi slipper for at skrive det fulde navn mange gange i løbet af en enkel notebook. Det er her vi bruger `as` nøgleordet. Når I gør dette, så brug dog gerne den konventionelle forkortelse (altså den som vi har brugt i cellen overfor), så vil det nemlig være nemmere for jer selv, jeres medstuderende og jeres instruktorer at læse og forstå den kode, som I skriver.

# ## Hvordan bruger man en pakke?
# 
# Når man har hentet sin pakke, kan man kalde de funktioner, som er i den. Hvis man har gjort som `curve_fit` ovenfor og kun importeret en enkelt funktion, kan man blot skrive `curve_fit(_input_)` i sin kode. Hvis man til gengæld har hentet en hel pakke, skal man også specificere pakken for at benytte en funktion. Man vil generelt skrive det som: `[forkortelse for pakke].[funktion]([variable]`. F.eks. giver `np.exp(2)` værdien af pakken np's eksponentialfunktion i punktet 2, altså $e^2$. 
# 
# Tænk på det som et bibliotek af funktioner. Numpy er biblioteket og exp er en bog i biblioteket. For at Python kan finde en funktion, skal du altså først fortælle, hvilket bibliotek Python skal gå til og derefter hvilken bog/funktion skal findes. Nogle biblioteker har også sektioner. Fx bruger vi udelukkende afdelingen "pyplot" af matplotlib-biblioteket.
# 
# Herunder kan man se nogle få eksempler på funktionskald:

# In[4]:


# Både sympy og numpy har de kendte trigonometriske funktioner samt værdien for pi
print(sp.cos(sp.pi)) 
print(np.cos(np.pi))


# In[6]:


x = np.linspace(0, 2 * np.pi, 1001) # denne funktion laver en liste af tal startende i 0, sluttende i 2*pi og med 1001 elementer
print(x)
y = np.cos(x)
plt.plot(x, y); # Plotter cosinus mellem 0 og 2 pi.


# Flere eksempler kan ses  herunder, hvor de mest brugte pakker: numpy, matplotlib og sympy er kort gennemgået. Dette er dog kun en oversigt, for at se en mere grundig gennemgang skal man finde noterne under enten "Python i Mekrel" eller "Python i LinAlys". 

# ## Numpy
# Numpy er den pakke, som vi bruger til numeriske udregninger. Helt centralt er numpy arrays, som er lister, der tillader os at udføre matematiske operationer på alle listens elementer samtidig. Vi starter med at importere numpy:

# In[9]:


import numpy as np


# Og vi kan nu tage en liste af nogle tal og konvertere til et numpy array:

# In[10]:


array_af_tal = np.array([1, 4, 9, 16, 25])
array_af_tal


# Hvis vi nu benytter en regneoperation, foretages operationen på alle elementerne:

# In[14]:


array_af_tal + 5 


# Derudover har numpy også en del indbyggede matematiske funktioner, som eksempelvis `cos`, `sin`, `sqrt` mm., som også kan bruges på enten et enkelt tal, eller på et helt array:

# In[15]:


np.sqrt(36)


# In[16]:


np.sqrt(array_af_tal)


# Yderligere benyttes numpy ofte til at lave statistik på et helt array, eksempelvis gennemsnittet af overstående array:

# In[17]:


np.mean(array_af_tal)


# For en mere grundig gennemgang af numpy i MekRel-sammenhænge, se [siden om numpy i MekRel](MekRel/Numpy.ipynb).

# ## Matplotlib Pyplot

# Matplotlib bruges til at plotte numeriske værdier, der f.eks. kunne være måledata fra laboratoriet. Vi importerer det ved:

# In[10]:


import matplotlib.pyplot as plt


# Herefter kan man nu benytte `plt.plot` til at plotte datapunkter: 

# In[18]:


x = np.array([1, 2, 3, 4, 5])
y = np.exp(x)

plt.plot(x, y, 'bo')
plt.title("Plot af punkter")
plt.xlabel("x")
plt.ylabel("y");


# Matplotlib kan desuden bruges til rigtig mange forskellige plottyper, og det er et super vigtigt værktøj i laboratoriet. Se hvordan det ellers bruges på [siden om matplotlib i MekRel](MekRel/Matplotlib_pyplot.ipynb).

# ## SymPy
# 
# Når vi skal foretage symbolske udregninger såsom at udregne grænseværdier, foretage differentialregning eller løse ligninger benytter vi SymPy. 
# 
# Når vi benytter SymPy starter vi oftest med at gøre Python opmærksom på, at vi ikke har med numeriske værdier at gøre, men i stedet noget mere abstrakt, som altså ikke skal afrundes eller udregnes, men lige præcis behandles som et symbol.
# 
# Først importerer man SymPy-biblioteket samt de symboler, som man gerne vil bruge fra ```sympy.abc```

# In[19]:


import sympy as sp                   # Importér biblioteket
from sympy.abc import x, a, b, phi   # Og de symboler som vi vil bruge. Vi kan altid hente flere   


# Vi kan nu kombinere symbolerne til nye udtryk.
# Eksempelvis kan vi danne et udtryk ved at gange og dividerer vores symboler med hinanden:

# In[20]:


a * b / x 


# Eller vi kan sammensætte de variable til nye variable:

# In[21]:


f = x * a * b
g = phi ** x 

display(f)
display(g)


# Her benytter vi ```display()``` i stedet for ```print()```, da dette viser symbolerne med matematisk formattering istedet for en tekst-version svarende til det, vi selv skrev ovenfor:

# In[23]:


print(g)


# Vi kan nu kombinere de to udtryk med hinanden:

# In[24]:


f * g ** (-f) - 1


# SymPy kommer nu også med en samling af funktioner, som vi kan bruge. Eksempelvis:

# In[26]:


display(sp.cos(x))                       # Udtryk med cosinus
display(sp.exp(f) ** 2 + sp.sqrt(g)** 2) # Udtryk med ekspoentialfunktionen og kvadratrødder 


# Der, hvor vi virkelig får glæde af SymPy er, når vi benytte det til differentiering, integration og til eksempelvis at finde grænseværdier. Betragt f.eks. funktionen:   
# $ f(x) = \frac{x^2 - 4}{x + 2} \cdot e^{-x}$  
# 
# kan vi benytte sympy til at finde grænseværdien for $f(x)$ for $x \rightarrow 2$:

# In[27]:


from sympy.abc import x
f = (x ** 2 - 4)/(x + 2)* sp.exp(-x)
sp.limit(f, x, 2)


# Vi kan også bestemme den afledte (eller differenterede) funktion:

# In[28]:


sp.diff(f, x)


# Eller det bestemte integral for $f(x)$ mellem grænserne $a$ og $b$:

# In[29]:


from sympy.abc import a, b
sp.integrate(f, (x, a, b))


# For en nøjere gennemgang af SymPy og de mange andre muligheder, som det tilbyder, referer vi til [noterne til python i LinAlys](sympy/Notebook1.ipynb).

# In[ ]:




