#!/usr/bin/env python
# coding: utf-8

# # Graftegning for funktioner af flere variable
# Så snart man bevæger sig op i flere dimensioner, begynder det at blive sværere at visualisere de funktioner, man arbejder med. SymPy har en række indbyggede funktioner, der især kan hjælpe os med at analysere funktioner af 2 variable. Den flade, som repræsenterer en funktion af to variable kan tegnes i 3 dimensioner, og vi vil også give eksempler på hvordan man tegner konturplot og niveaukurver.
# 

# ## Graftegning i 3D
# For at tegne flader i 3D starter vi på samme måde som vi gjorde for 2D-tilfældet, men i stedet for at importere <code>plot</code> fra <code>sympy.plotting</code>, importerer vi nu i stedet <code>plot3d</code>. Herefter kan vi skrive <code>plot3d(expr, (x, y))</code> eller f.eks. <code>plot3d(expr, (x, -2, 2), (y, -2, 2))</code> hvis vi vil bestemme akseskaleringen. Der er oftest nødendigt at kunne rotere flader i 3D for at få et fyldestgørende indtryk af figures, så vi benytter her <code>%matplotlib notebook</code> som gør vores figurer interaktiv. Hvis man eksempelvis vil plotte $xy^2$ i området omkring origo, kan man gøre følgende:

# In[17]:


from sympy.plotting import plot3d         # importer plot3d
# Aktiver interaktiv egentskab'
get_ipython().run_line_magic('matplotlib', 'notebook')

expr = x * y**2                           # Definer udtryk
plot3d(expr, (x, -2.5, 2.5), (y, -2, 2));     # Plot med fastsatte akse-intervaller


# Python-SymPy-kombinationen har en meget uheldig svaghed her, idet det ikke umiddelbart er nemt at tilføje akselabels. Et workaround er at vælge forskellige akseskaleringer for $x$-aksen og $y$-aksen, så man kan se forskel også når man har roteret grafen.

# ## Konturer

# Konturplot findes ved at lave en 2D-afbildning af værdien af den pågældende funktion af flere variable langs en linje. I tilfældet med en funktion af 2 variable ligger linjen i $xy$-planen, og konturen svarer til grafens skæring med den plan, der kan rejses vinkelret på $xy$-planen og som indeholder den pågældende linje. Se TK afsnit 1.2.1. De simpleste konturer fås ved at holde værdien af enten $x$ eller $y$ fast og så plotte $f(x,y)$ som funktion af den anden variabel. Vi vil her følge TK eksempel 1.6 og betragter funktionen:
# $$f(x,y) = 2x^2+ 4x - y^2 + 4y$$
# Vi kan altså lave et konturplot ved at kigge på funktionens variation med $x$ mens vi eksempelvis sætter $y = 1$:

# In[9]:


from sympy.plotting import plot

# Definer funktion
f = 2 * x ** 2 + 4 * x - y ** 2 + 4 * y

# Lav et plot
plot(f.subs(y, 1), (x, -5, 5));


# For at få en fornemmelse af grafen for f, er et enkelt sådan snit ikke nok, så vi vil gerne lave en serie af konturplots. Vi kan her bruge <code>PlotGrid</code> fra <code>sympy.plotting</code>, som lader os sammensætte flere plots i en gitterstruktur. Vi bruger funktionen ved at at sige <code>PlotGrid(antal_rækker, antal_kolonner, plot1, plot2 ...)</code> 
# Vi kan altså nu lave flere plots og så sætte dem sammen. Hvis vi nu vil lave seks plots hvor $y = -1,...,4$ kan vi lave de enkelte grafen i en løkke og sætte dem sammen til sidst:

# In[10]:


y_værdier = [-1, 0, 1, 2, 3, 4] # Definer liste
figurer   = []           # Tom liste til figurer

for y_val in y_værdier:  # Pas på med at skrive y her, da vi allerede bruger den som symbol-variabel
    figur = plot(f.subs(y, y_val), show = False)   # Indsæt værdien af y og plot uden at vise grafen
    figur.axis_center = (0,0)                      # For at gøre de enkelte grafer ens, sætter vi den samme akseskæring
    figur.xlim = (-4, 4)                           # ... og samme akseafgrænsinger for x-aksen
    figur.ylim = (-15, 20)                         # ... og y-aksen
    figur.title = "y = {}".format(y_val)           # Tilføj titel til plot
    figurer.append(figur)                          # Vi tilføjer figuren til en liste af figurer
    
from sympy.plotting import PlotGrid            # Importer gitterplottefunktion
PlotGrid(2, 3, *figurer);                      # Nu samler vi de 6 figurer i et gitterplot


# Det er værd at lægge mærke til at vi eskplicit sætter akseafgrænsningen til at være ens for alle 6 grafer. Ellers vil Python skalere dem fra figure til figur efter de enkelte grafers placering, hvilket vil gøre det svært at sammenligne de seks plots. Stjernen foran listen <code>figurer</code> svarer til <code>figurer[0], figurer[1] ... </code>, og er altså en genvej til at skrive alle elementerne i <code>figurer</code> op.
#     
# Vi kan nu gentage overstående, men skifte x-værdier:

# In[11]:


x_værdier = [-4, -3, -2, -1, 0, 2]  # nu er det en liste af x-værdier
figurer   = []     

for x_val in x_værdier:
    figur = plot(f.subs(x, x_val), show = False)   # Indsætter nu værdier for x i stedet
    figur.axis_center = (0,0)                      
    figur.xlim = (-2, 6)                           # sæt nye mere passende grænser       
    figur.ylim = (-15, 20)                         # også her
    figur.title = "x = {}".format(x_val)           # Skriv nu "x =" i titlen 
    figurer.append(figur)                          
    
PlotGrid(2, 3, *figurer);                      # Nu samler vi de 6 figurer i et gitterplot


# ## Niveaukurver

# Mens konturer er snit mellem grafen for en funktion og "opretstående planer", er niveaukurver snit med vandrette planer $z=c$ (se TK 1.2.2). Vi vil altså tegne løsninger til $f(x,y) = c$ i $xy$-planen. I SymPy kan vi få et hurtigt overblik ved at benytte funktionen <code>plot_contour</code> (bemærk at <code>plot_contour</code> her bliver brugt til at tegne niveaukurver og _ikke_ konturplot) som importeres fra <code>sympy.plotting.plot</code>. Funktionen følger samme syntaks som <code>3dplot</code>, og giver os et bud på, hvordan niveaukurverne ligger. Desværre har vi ret begrænsede muligheder for selv at vælge indstillinger for denne funktion.
# 
# Her undersøger vi (ligesom i TK 1.10) funktionen:
# $$ f(x, y) = x^2 + 4y^2 $$
# 

# In[12]:


from sympy.plotting.plot import plot_contour
f = x ** 2 + 4 * y ** 2

niveau = plot_contour(f, (x, -5, 5), (y, -5, 5));


# Linjerne i plottet markere altså de sammenhængende $(x,y)$-værdier, hvor $f$ antager en bestemt værdi. Da funktionen her er meget ny i Python og ikke helt færdigudviklet, er det desværre ikke muligt at bestemme hvilken værdier, linjerne skal tegnes ved. Til gengæld har vi også muligheder for selv at gøre arbejdet. Vi kan nemlig benytte sympy til at tegne såkaldte implicitte udtryk, altså eksempelvis alle punkter i $xy$-planen, der opfylder, at $f(x,y) = c$ for et givet c. 
# 
# Vi betragter nu (jvf TK 1.11) $f$ givet ved:
# $$f(x,y) = x^2 - xy + y$$
# 
# Vi benytter <code>plot_implicit</code> fra <code>sympy.plotting</code> til at finde niveaukurven for $c = 3$. Vi danner først en ligning ved at skrive <code>sp.Eq(udtryk, c)</code> og så grænser for, hvor den skal plotte det henne, på samme måde som <code>contour_plot</code> og <code>plot3d</code>.

# In[13]:


f = x ** 2 - x * y + y

from sympy.plotting import plot_implicit
plot_implicit(sp.Eq(f, 3), (x, -5, 5), (y, -5, 5));


# Hvis vi vil tegne niveaukurve for værdier, vi selv kan bestemme, kan vi på samme måde som ved konturplottene lave en løkke, hvor vi går igennem de ønskede værdier:

# In[14]:


c_værdier = [-3, -1, 1, 3, 5]

# Hvis vi vil tegne i samme figur, skal vi starte med at lave en figur. Lad os bare lave en figur med den første niveaukurve
figur = plot_implicit(sp.Eq(f, 1), show = False, xlim = (-4, 6), ylim= (-3, 7))

for c_val in c_værdier:   # loop over vores liste
    ny_figur = plot_implicit(sp.Eq(f, c_val), show = False)
    figur.append(ny_figur[0])

figur.show()


# Bemærk her, at vi egentlig plotter for $c = 1$ to gange, første gang da vi opretter figuren, og derefter ved første gennemløb i løkken. Dette vil dog i næsten alle tilfælde ikke være et problem, da vi blot tegner den samme kurve to gange oveni hinanden. Hvis man ikke ønsker dette, kan man fjerne det første element for listen. 

# Vi ser at Python finder at $f=1$ ikke kun er opfyldt langs linjerne $x = 1$ og $y=1+x$ (hvilket vi nemt kan indse ved at indsætte i udtrykket for $f$), men også i et område nær hvor disse to linjer krydser. Dette skyldes at Python/SumpY løser $f(x,y)=c$ numerisk med en given (og tilsyneladende ikke ret høj) opløsning. Ved at betragte $f$ i 3D kan vi se at funktionen rigtigt nok er meget flad omkring $(x,y)=(1,2)$:

# In[19]:


figur = plot3d(f, (x, 0.8, 1.2), (y, 1.8, 2.2));


# For at plotte kurverne med $f(x,y) = 1$ benytter vi at sympy bygger på matplotlib, så vi kan lave et numerisk plot ovenpå et sympy-plot ved at kalde <code>figur._backend.ax[0]</code>, hvorefter vi kan bruge <code>plot(xs, ys, zs)</code> fra matplotlib. SymPy-begyndere behøver ikke bekymre sig om detaljerne :o)

# In[16]:



from sympy.abc import u
import numpy as np
from sympy.plotting import plot3d_parametric_line

xs = np.ones(100)
ys = np.linspace(1.75, 2.25, 100)
zs = np.ones(100)


figur._backend.ax[0].plot(xs, ys, zs, color = 'red')

xs = np.linspace(0.75, 1.25, 100)
ys = 1 + np.linspace(0.75, 1.25, 100)
zs = np.ones(100)

figur._backend.ax[0].plot(xs, ys, zs, color = 'red')

figur._backend.fig

