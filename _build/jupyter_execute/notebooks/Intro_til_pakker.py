#!/usr/bin/env python
# coding: utf-8

# # Intro til pakker
# 
# Python er et af de mest brugte programmering sprog i verden specielt i den akademiske verden. Derfor er der også en kæmpe mængde pakker, som kan løse alverdens problemer. Her i starten skal i stifte bekendskab med 4:
#  * Sympy ([dokumentation](https://www.sympy.org/en/index.html))
#  * Numpy ([dokumentation](https://numpy.org/doc/stable/))
#  * Matplotlib ([dokumentation](https://matplotlib.org/stable/index.html))
#  * Scipy ([dokumentation](https://docs.scipy.org/doc/scipy/reference/))
# 
# Det ligger næsten i navnet hvad de kan og hvad de skal bruges til:
#  * Sympy (Symbolic Python) er til symbolsk matematik
#  * Numpy (Numerical Python) er til numeriske beregninger
#  * Matplotlib (Mathematical ploting library) er til at lave plots 
#  * Scipy (Scientific Python) her skal vi kun bruge en funktion
# 
# Ligesom det er vigtigt at bruge den rigtige metode til at løse en ligning, er det ligeså vigtigt at bruge den rigtige pakke til et programmeringsproblem. Som tommelfingerregel skal I bruge Sympy i LinAlys til at foretage symbolske udreginger for at kontrollerer svar og lave nogle simple plots af funktioner. I laboratoriet skal I bruge Numpy og Matplotlib til at behandle og illustrerer jeres data fra og Scipy til at lave fits.
# 
# Nogle af pakkerne har noget overlap, og de er lavet til at kunne bruges sammen. Til at starte med, vil vi dog prøve at undgå dette, da det hurtig kan blive meget kompliceret og nok en god kilde til fejl i koden. 
# 

# ## Import 
# 
# For at hente en af de 4 ovenstående pakker ind i et python benytter vi os af `import` nøgleordet, som fortæller python, at funktionerne skal hentes fra den pågældende pakke. Med `as` kan vi desuden give dem et navn, så vores navn bliver en smule nemmere. Vi kan hente de fire pakker ved at skrive følgende i en celle: (i `scipy.optimize` specificerer vi her, at vi kun vil hente én funktion derfra, `curve_fit`) 
# 

# In[1]:


import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Selvom det er fristende, altid at hente alle pakkerne ind. Så er det en fordel kun at hente de pakker ind, som man skal bruge. Dette vil både gøre koden hurtigere, hvis ikke den skal til at hente et stort bibliotek af funktioner, for at man bruger en funktion, men det er også en fordel, hvis andre personer skal læse koden, at man tydeligt kan se, hvilke pakker udefra som skal bruges for at køre koden.  

# Nogle pakker bruger vi så ofte, at vi gerne forkorter deres navne, så vi slipper for at skrive det fulde navn mange gange i løbet af en enkel notebook. Det er her vi bruger `as` nøgleordet. Når I gør dette, så brug dog gerne den konventionelle forkortelse (altså den som vi har brugt i cellen overfor), så vil det nemlig være nemmere for jer selv, jeres medstuderende og jeres instruktorer at læse og forstå den kode, som I skriver.

# ## Hvordan bruger man en pakke?
# 
# Når man så har hentet sin pakke ind, kan man kalde de funktioner, som der er i den. Hvis har man har gjort som `curve_fit` ovenover, kan man blot skrive `curve_fit(_input_)` i sin kode. Hvis man tilgengæld har hentet en hel pakke, skal man også specificere pakken for at benytte en funktion. Man ville generelt skrive det op som: `[forkortelse for pakke].[funktion]([variable]` f. eks. `np.exp(2)` giver $e^2$. Herunder kan man se nogle få eksempler:

# In[2]:


# Både sympy og numpy har de kendte matematiske funktioner husk ikke at blande dem.
print(sp.cos(sp.pi)) 
print(np.cos(np.pi))


# In[20]:


x = np.linspace(0, 2 * np.pi, 1000)
y = np.cos(x)
plt.plot(x, y);


# Flere eksempler kan ses  herunder, hvor de mest brugte pakker: numpy, matplotlib og sympy er kort gennemgået. Dette er dog kun en oversigt, for at se en mere grundig gennemgang skal man finde noterne under enten "Python i Mekrel" eller "Python i LinAlys". 

# # Numpy
# Numpy er den pakke, som vi bruger til numeriske udregninger. Helt centralt er numpy arrays, som er lister, der tillader matematiske operationer på alle elementer samtidig. Vi starter med at importerer numpy:

# In[4]:


import numpy as np


# Og vi kan nu tage et liste af nogle tal og konverterer til et numpy array:

# In[5]:


array_af_tal = np.array([1, 4, 9, 16, 25])
array_af_tal


# Hvis vi nu benytter dette array i regne operation, foretages operationer på alle elementer af gangen:

# In[6]:


array_af_tal + 5 


# Derudover har numpy også en del indbygget matematiske operationer, som eksempelvis `cos`, `sin`, `sqrt` mm., som også kan bruges på enten et enkelt tal, eller på et helt array:

# In[7]:


np.sqrt(36)


# In[8]:


np.sqrt(array_af_tal)


# Yderligere benyttes numpy ofte til at regne statistik på et helt array, eksempelvis gennemsnittet af overstående array:

# In[9]:


np.mean(array_af_tal)


# En mere grundig gennemgang af numpy i MekRel sammenhænge se [side om numpy i mekrel](Mekrel/Numpy.ipydb).

# # Matplotlib Pyplot

# Matplotlib bruges til at plotte numeriske værdier fra eksempelvis laboratoriet. Vi importerer det ved:

# In[10]:


import matplotlib.pyplot as plt


# Herefter kan man nu benytte `plt.plot` til at plotte datapunkter: 

# In[11]:


x = np.array([1, 2, 3, 4, 5])
y = np.exp(x)

plt.plot(x, y, 'bo')
plt.title("Plot af punkter")
plt.xlabel("x")
plt.ylabel("y");


# Matplotlib kan desuden bruges til rigtig mange forskellige plot typer, og det er et super vigtigt værktøj i laboratoriet. Se hvordan det ellers bruges på [siden om matplotlib i MekRel](MekRel/Matplotlib_pyplot.ipynb).

# # SymPy
# 
# Når vi skal foretage symbolske udregninger såsom at udregne grænser, foretage differentialregning eller løse ligninger benytter vi SymPy. 
# 
# Når vi benytter SymPy starter vi oftest med at gøre Python opmærksom på, at vi ikke har med numeriske værdier at gøre, men i stedet noget mere abstrakt, som altså ikke skal afrundes eller udregnes, men lige præcis behandles som et symbol.
# 
# For at starte op i SymPy importerer man biblioteket samt de symboler, som man gerne vil bruge fra ```sympy.abc```

# In[12]:


import sympy as sp                   # Importer biblioteket
from sympy.abc import x, a, b, phi   # Og de symboler som vi vil bruge. Vi kan altid hente flere   


# Når man nu benytter sympy kan blot kombinerer symbolerne til nye udtryk. Eksempelvis kan vi danne et udtryk  ved at gange og dividerer vores symboler med hinanden:

# In[13]:


a * b / x 


# Eller vi kan sammen sætte dette i nye udtryk, som vi nu kan behandle sammen:

# In[14]:


f = x * a * b
g = phi ** x 

display(f)
display(g)


# Her benytter vi ```display()``` i stedet for ```print()```, da vi ikke vil have en tekst version af vores symboler, men i stedet fortæller vi jupyter, at symbolerne skal skrives. Vi kan nu kombinere de to udtryk med hinanden:

# In[15]:


f * g ** (-f) - 1


# SymPy kommer nu også med en samling af funktioner, som vi kan bruge. Eksempelvis:

# In[16]:


display(sp.cos(x))                       # Udtryk med cosinus
display(sp.exp(f) ** 2 + sp.sqrt(g)** 2) # Udtryk med ekspoential funktioner og kvadratrødder 


# Der, hvor vi virkelig får glæde af SymPy er, når vi benytte det til differentiering, integration og til eksempelvis at finde grænser. Hvis vi nu har funktionen:   
# $ f(x) = \frac{x^2 - 4}{x + 2} \cdot e^{-x}$  
# 
# Kan vi benytte sympy til at finde grænser for $x \longrightarrow 2$

# In[17]:


from sympy.abc import x
f = (x ** 2 - 4)/(x + 2)* sp.exp(-x)
sp.limit(f, x, 2)


# Den afledte funktion:

# In[18]:


sp.diff(f, x)


# Eller til integration:

# In[19]:


from sympy.abc import a, b
sp.integrate(f, (x, a, b))


# For en nøjere gennemgang af SymPy og de mange andre muligheder, som det tilbyder, referer vi til [noterne til python i LinAlys](sympy/Notebook1.ipyndb).
