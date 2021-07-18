#!/usr/bin/env python
# coding: utf-8

# <h1>Indholdsfortegnelse<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Funktioner" data-toc-modified-id="Funktioner-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Funktioner</a></span></li><li><span><a href="#Fitting" data-toc-modified-id="Fitting-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Fitting</a></span></li></ul></div>

# # Functioner, fits og usikkerheder i python
# 

# I denne note vil vi introducere jer til funktioner, hvordan man fitter en model til data og behandler usikkerheder i Python. 

# ## Funktioner

# Før vi kan fitte en funktion med Python skal vi kunne definere en funktion. En funktion er et meget bredt begreb i Python og man kan rigtig meget med dem, og når I kommer lidt længere i jeres udannelse er det hovedsageligt dem I skal bruge når I programmerer, men lige nu skal vi bare kunne bruge dem til at fitte. 
# 
# Man definerer en funktion ved at skrive 'def', skrive det funktionen skal gøre, også skrive 'return', hvor man skriver det funktionen skal levere. Et eksempel ses under.

# In[1]:


def funktion(m,v):
    return 1/2 * m * v**2


# Her har jeg defineret en funktion som jeg kalder funktion, den tager 2 argumenter, m og v, og returnerer $ \frac{1}{2}  m v^2$. Den kan vi så prøve af for m = 80 og v = 5

# In[2]:


print(funktion(80,5))


# Funktioner kan også bruges til at gøre kode mere overskuelig og nemmere at debugge, her er der fx defineret en funktion som laver et plot. Den tager ingen værdier og retunere heller ikke noget, men er nem at debugge og man kan lade være med at kalde den når man har fået sit plot.

# In[3]:


import numpy as np

v_data = np.linspace(0,100,1000)
E_data = funktion(80,v_data)

def plot_E_kin():
    import matplotlib.pyplot as plt
    plt.plot(v_data,E_data, label = 'Energi')
    plt.xlabel('Fart [m/s]')
    plt.ylabel('Energi [J]')
    plt.legend()
    plt.show()
    plt.close('all')

plot_E_kin()


# ## Fitting

# Vi skal nu bruge funktioner til at fitte en model til data. Her bruger vi optimize.curve_fit, denne kommer fra pakken SciPy og importeres således.

# In[4]:


from scipy.optimize import curve_fit


# For at fitte en model skal man have noget data at fitte til, her bruger jeg den data der lå på jeres første Python aflevering.

# In[5]:


data = np.array([
    [0.19,1.98,2.05,2.16,2.16,2.07],
    [0.3,2.61,2.6,2.58,2.81,2.68],
    [0.36,3,3,3,2.87,2.97],
    [0.53,3.47,3.83,3.54,3.6,3.5],])
print(data)


# For at fitte en model til data, skal man have ét datapunkt for hver varieret måling, her har vi 5 målinger per pendullængde, derfor skal vi altså tage gennemsnit af vores svingningstider.

# In[6]:


L = data[: , 0] #udvælger kolonnen med pendullængde
svingningstider = data[:,1:5] #her udvælger vi de fire kolonner  med svingningstider

gns_svingning = np.mean(svingningstider, axis = 1) #tager gennemsnit af svingningstiderne, "axis" angiver om vi går vandret eller lodret i datasættet

print(L)
print(gns_svingning)


# Nu har vi to lister med data punkter der hænger sammen, nu kan vi begynde at undersøge hvilket fit vi skal bruge. Vi regner med at skulle bruge en lineær funktion, så vi skal have defineret det i vores kode. Vi kalder funktionen "linfunc", og angiver så variabel og parametre i parentes. I return skriver vi hvad funktionen skal give som resultat når vi bruger den.

# In[7]:


def linfunc(x,a,b):
    y = a*x + b
    return y


# Når man fitter er det meget **vigtigt** at det første argument i ens funktion, her x, er det som man har data på og vil have python til at fitte efter, ellers fungerer fittet ikke. Dette er en fejl som ofte opstår, så hvis I får en fejl så tjek lige om i har det rigtige stående som det første i jeres parentes.
# 
# Når man så har en funktion defineret rigtigt, kan man fitte vores funktion til dataen med kommandoen optimize_curvefit. Funktionen optimize.curve_fit skal bruge funktionen der ønskes at fitte efter, også de tilhørende x- og y-værdier, i dette tilfælde pendullængde og svingningstid. Funktionen giver to outputs, først giver den fitte-paramterene, det vil sige fittets bedste bud på hvad parametrene i fit-funktionen bør være. Dernæst giver den covariansen. Er der flere parametre angives covariansen som en matrix med flere værdier. Covariance matrixen kan bruges til at finde ussikerheder på fit parametre, men mere om det til sidst.

# In[8]:


par, cov = curve_fit(linfunc, L , gns_svingning)
print(par) #printer parametrene
print(cov) #printer covariansen


# Nu kan vi plotte vores data sammen med vores fit, og vurdere hvor god vores model er. Vi skal selvfølgelig også have plottet vores usikkerheder, og da vi arbejder med gennemsnit vil vi plotte usikkerheden ved hjælp af standardafvigelsen på vores data. Man kan bruge NumPy funktionen np.std() til at bestemme standardafvigelse.
# 
# For at plotte vores fit laver vi et array af værdier i det interval vi gerne vil plotte med np.linspace funktionen. Vi bruger så disse værdier i vores lineære-funktion, hvor vi bruger de parametre vores fit bestemte med optimize.curve-fit.

# In[9]:


import matplotlib.pyplot as plt

afvigelse = np.std(svingningstider, axis = 1)/np.sqrt(len(svingningstider))

X = np.linspace(0.1,0.6,1000) #laver et array af 1000 jævnt fordelte tal mellem 0.1 og 0.6
Y = linfunc(X,par[0],par[1])  #laver et array af vores lineære fit på det ovenstående array

plt.plot(L , gns_svingning, '.', label = 'Data')
plt.plot(X,Y , label = 'Fit')
plt.errorbar(L , gns_svingning , yerr=afvigelse , fmt='none' , label = 'Usikkerhed')
plt.xlabel('Snorlængden [m]')
plt.ylabel('Sviningstid [s]')
plt.title("Svingningstid som funktion af snorlængde")
plt.legend()
plt.show()


# Man kan også lave et fit, hvor der tages højde for usikkerheden på datapunkterne. Det gør man ved at angive et sigma når man bruger curve_fit.

# In[10]:


par_with_error, cov_new = curve_fit(linfunc, L , gns_svingning, sigma = afvigelse)
print(par_with_error)


# Paremeterne er ikke ændret så meget da fejlen på punkterne er meget ens, men hvis der havde været stor forskel på usikkerhederne ville det have en større effekt. Endeligt kan man så plotte punkter med usikkerheder og fit som tager højde for usikkerheden.

# In[11]:


Y_2 = linfunc(X,par_with_error[0],par_with_error[1])

plt.errorbar(L , gns_svingning,yerr= afvigelse, fmt='.', label = 'Data')
plt.plot(X,Y_2 , label = 'Fit')
plt.xlabel('Snorlængden [m]')
plt.ylabel('Sviningstid [s]')
plt.legend()
plt.title("Svingningstid som funktion af snorlængde")
plt.show()


# For at finde ussikerheden på de fit parametre som er fundet her kan man bruge covariance matrixen. På dens diagonal er nemlig variancen for de fittede parametre. Når man har variancen kan man finde ussikerheden da kvadratroden af variancen er ussikerheden. I python kan det gøres med et for loop

# In[12]:


for i in range(len(cov_new)):
    sigma = np.sqrt(cov_new[i,i])
    print(par[i], ' +/-' , sigma)
    


# Her er fit værdierne for a og b printet med ussikerheder fundet fra covariance matrixen.
