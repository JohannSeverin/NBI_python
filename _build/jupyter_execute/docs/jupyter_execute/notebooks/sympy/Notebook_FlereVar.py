#!/usr/bin/env python
# coding: utf-8

# <h1>Indholdsfortegnelse<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Differentiation-af-funktioner-af-flere-variable" data-toc-modified-id="Differentiation-af-funktioner-af-flere-variable-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Differentiation af funktioner af flere variable</a></span><ul class="toc-item"><li><span><a href="#Partielt-afledede" data-toc-modified-id="Partielt-afledede-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Partielt afledede</a></span></li><li><span><a href="#Gradienter-og-retningsafledede" data-toc-modified-id="Gradienter-og-retningsafledede-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Gradienter og retningsafledede</a></span></li><li><span><a href="#Hessematricen" data-toc-modified-id="Hessematricen-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Hessematricen</a></span></li></ul></li><li><span><a href="#Graftegning-for-funktioner-af-flere-variable" data-toc-modified-id="Graftegning-for-funktioner-af-flere-variable-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Graftegning for funktioner af flere variable</a></span><ul class="toc-item"><li><span><a href="#Graftegning-i-3D" data-toc-modified-id="Graftegning-i-3D-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Graftegning i 3D</a></span></li><li><span><a href="#Konturer" data-toc-modified-id="Konturer-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Konturer</a></span></li><li><span><a href="#Niveaukurver" data-toc-modified-id="Niveaukurver-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Niveaukurver</a></span></li></ul></li></ul></div>

# # Funktioner af flere variable

# Vi har nu udvidet vores funktionsdefinition til at omfatte funktioner af flere variable. Som udgangspunkt kan vi bruge Python/SymPy på samme måde som for funktioner af en variabel. Vi tilføjer dog de variable $y$ og $z$  til vores standard startblok:

# In[1]:


import sympy as sp                    # Importer sympy
from sympy import Matrix              # Importer den korte form at definere matricer på
from sympy.abc import x, y, z         # Vi henter vores variabler
from sympy import oo, pi, I           # Vi importerer uendelig, pi og den imaginære konstant I 
sp.init_printing()                    # Aktiver pretty-printing
from IPython.display import display   # Hent vores printer til matematiske udtryk


# ## Differentiation af funktioner af flere variable

# For funktioner af flere variable bliver diffentialkvotienterne $f'$, $f''$ afløst af lidt flere begreber. Vi vil i det følgende demonstrere hvordan man beregner partielt afledede, gradienter og Hesse-matricer (som dog først bliver berørt til sidst i LinAlys-kurset).
# 
# ### Partielt afledede
# Når vi går fra en til flere variable, spiller de partielt afledede en central rolle. De beregnes på en helt tilsvarende måde som vi tidligere har beregnet $f'$, idet vi blot skal være opmærksomme på, hvilken variabel, vi differentiere i forhold til. Vi har også ved differentiation af funktioner af en variabel (se notebook til uge 4) angivet navnet på den variable, f.eks. <code>sp.diff(expr, x)</code>, men dette var faktisk ikke strengt nødvendigt for simple funktioner, da SymPy i mange tilfælde kan gætte hvad der er den variable. Når vi har to variable, er det derimod afgørende at vi angiver den relevante variabel eksplicit.
# 
# Ellers foregår mange beregninger på samme måde:

# In[2]:


expr = sp.sin(x**2 * y)         # Vi definerer vores funktion af de to variable x og y
display(sp.diff(expr, x))       # Og differentierer, som vi plejer ift x
display(sp.diff(expr, y))       # Og i forhold til y


# Derimod giver <code>display(sp.diff(expr))</code> en fejlmeddelelse. Vi kan også differentiere flere gange efter hinanden i én kommando: Hvis vi f.eks. ønsker at udregne $\frac{\partial^2}{\partial x \partial y}\left ( x^2\cdot e^y\right )$, skriver vi <code>sp.diff(expr, y, x)</code>. Bemærk rækkefølgen af $x$ og $y$ her: i $\frac{\partial^2}{\partial x \partial y}$ står $\partial y$ bagerst, og logikken er, at da dette er nærmest funktionsudtrykket, skal vi differentiere efter $y$ først. Mere formelt er $\frac{\partial^2f}{\partial x \partial y} \equiv \frac{\partial}{\partial x}\left ( \frac{\partial f}{\partial y} \right )$. Syntaksen i Python er derimod at de variable skal listes  i differentiations/integrationsrækkefølgen i almindelig læseretning. Dette giver os:

# In[3]:


expr = x**2*sp.exp(y)
display(sp.diff(expr, x))
display(sp.diff(expr, x, y))
display(sp.diff(expr, y))
display(sp.diff(expr, y, x))


# ### Gradienter og retningsafledede

# Et centralt begreb for funktioner af flere variable er gradienten, som vi skriver som $\nabla f(x,y) = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$. Vi tager altså den partielle differentieret i forhold til vores variable og sætter dem sammen som en vektor. 
# 
# Der er flere måder at beregne gradienten på i Python/SymPy, men her vil vi anvende en måde, der læner sig op af den måde, vi udregner den på i hånden. Vi vil altså lave en vektor bestående af de forskellige partielt afledede. Vi gør dette med <code>sp.derive_by_array()</code>, der som input skal bruge en funktion og en liste af de variable, der skal differentieres efter.
# 
# 
# Eksempel: Vi vil finde gradienten af $f(x,y) = e^{- x^2 - y^2}$.

# In[4]:


expr = sp.exp(- x ** 2 - y ** 2)

grad = sp.derive_by_array(expr, [x, y])
display(grad)


# Resultatet kan umiddelbart aflæses, men hvis vi vil regne videre med gradienten som en vektor, bliver vi nødt til at benytte <code>sp.Matrix()</code> til at konvertere resultatet til matrixform, som vi kender fra notebooken om Linær Algebra.
# 
# Lad os nu eksempelvis beregne den retningsafledede for ovenstående funktion i retningen $\left(\frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}}\right)$ i punktet med $(x, y) = (1, 2)$. Vi beregner nu jvf. TK sætning 2.57:

# In[5]:


grad_vec = Matrix(grad)       # Kovnerterer til vektor/matrix-format
display(grad_vec)             # Vi viser det lige

# Vi definerer retningsvektoren i vektorformat
retning = Matrix([1/sp.sqrt(2), 1/sp.sqrt(2)])
display(retning)

# Vi beregner prikproduktet mellem gradienten med retningsvektoren
prikket = grad_vec.dot(retning)
display(prikket)

# Vi indsætter x = 1 og y = 2 med .subs
resultat = prikket.subs(x, 1).subs(y, 2)
display(resultat)


# ### Hessematricen
# Sidst i kurset vil vi bruge den såkaldte Hessematrix, der er en $n\times n$-matrix, der indeholder alle andenordens afledede for en funktion af $n$ variable. Vi vil specielt bruge determinanten af Hessematricen til at undersøge opførslen af funktioner af 2 variables omkring et stationært punkt (se TK sætning 3.4, der som det fremgår af kommentaren lige under sætningen kan formuleres ved hjælp af Hessematricen).
# 
# Man kunne beregne Hessematricen ved at beregne de dobbelt afledede som beskrevet ovenfor, men det er nemmere at importere den fra underbiblioteket af SymPy, som hedder <code>sympy.matrices</code> med kommandoen <code>from sympy.matrices import hessian</code>. Vi kan nu benytte <code>hessian(udtryk, variabelliste)</code> på samme måde, som vi brugte <code>sp.derive_by_array</code> til at udregne gradienten:

# In[6]:


from sympy.matrices import hessian        # Importer Hessematricen
expr = sp.exp(- x ** 2 - y ** 2)          # Definer samme funktion som tidligere

H = hessian(expr, [x, y])
display(H)


# Og hvis vi nu vil beregne værdien for $(x, y) = (0, 1)$, kan vi benytte <code>.subs()</code> to gange:

# In[7]:


H.subs(x, 0).subs(y, 1)


# ## Graftegning for funktioner af flere variable
# Så snart man bevæger sig op i flere dimensioner, begynder det at blive sværere at visualisere de funktioner, man arbejder med. SymPy har en række indbyggede funktioner, der især kan hjælpe os med at analysere funktioner af 2 variable. Den flade, som repræsenterer en funktion af to variable kan tegnes i 3 dimensioner, og vi vil også give eksempler på hvordan man tegner konturplot og niveaukurver.
# 

# ### Graftegning i 3D
# For at tegne flader i 3D starter vi på samme måde som vi gjorde for 2D-tilfældet, men i stedet for at importere <code>plot</code> fra <code>sympy.plotting</code>, importerer vi nu i stedet <code>plot3d</code>. Herefter kan vi skrive <code>plot3d(expr, (x, y))</code> eller f.eks. <code>plot3d(expr, (x, -2, 2), (y, -2, 2))</code> hvis vi vil bestemme akseskaleringen. Der er oftest nødendigt at kunne rotere flader i 3D for at få et fyldestgørende indtryk af figures, så vi benytter her <code>%matplotlib notebook</code> som gør vores figurer interaktiv. Hvis man eksempelvis vil plotte $xy^2$ i området omkring origo, kan man gøre følgende:

# In[17]:


from sympy.plotting import plot3d         # importer plot3d
# Aktiver interaktiv egentskab'
get_ipython().run_line_magic('matplotlib', 'notebook')

expr = x * y**2                           # Definer udtryk
plot3d(expr, (x, -2.5, 2.5), (y, -2, 2));     # Plot med fastsatte akse-intervaller


# Python-SymPy-kombinationen har en meget uheldig svaghed her, idet det ikke umiddelbart er nemt at tilføje akselabels. Et workaround er at vælge forskellige akseskaleringer for $x$-aksen og $y$-aksen, så man kan se forskel også når man har roteret grafen.

# ### Konturer

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


# ### Niveaukurver

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


# 
