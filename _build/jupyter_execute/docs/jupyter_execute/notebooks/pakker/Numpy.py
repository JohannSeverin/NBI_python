#!/usr/bin/env python
# coding: utf-8

# # Numpy
# 
# Numpy bruges til at lave nummeriske beregniner og vil være jeres primære værktøj i laboratoriet. Det skyldes at man kan bruge `numpy arrays`. Det er en data type som gør operationer på mange tal hurtigt og forhåbenlig intuativt når i har arbejdet lidt med det.
# 

# 
# ## Numpy arrays
# 
# For at lave et numpy array kan man skrive forskelige ting her er nogle eksempler,
# 

# In[2]:


import numpy as np # Husk at importere numpy ellers virker det ikke.


# In[3]:


array1 = np.array([3,4,5,1]) #manuelt indtastede værdier
array2 = np.arange(0,3,0.5) #et array med tallene fra 0 til 3 (ekslusiv 3) i 0.5 skridtstørrelse
array3 = np.linspace(0,8,5) #et array med tallene fra 0 ti 8 (inklusiv 8) i 5 skridt

print(array1) #ønsker du at se noget af det du har defineret så "print" det således
print(array2)
print(array3)


# Læg mærke til at NumPy funktionen arange tæller efter skridtstørrelse, altså hvor stort mellemrum der skal være mellem hver værdi i intervallet man angiver, og linspace tæller efter hvor mange skridt der skal være i alt, og giver så en jævn fordeling af værdier i det interval man angiver.
# 
# Vil man gerne trække tal ud af sine arrays, gøres det ved at skrive indekset på det man gerne vil have ud,

# In[4]:


array4 = np.array([3,4,5,1,6,8]) #Definerer et array
print(array4)

print( array4[0], array4[2]) #vælger den første og tredje værdi i arrayet

print(array4[1:5]) #vælger værdien fra indeks 1 til og uden 5 (husk at Python indekserer fra 0)

print(array4[-1]) #man kan også vælge den sidste værdi ved at tælle baglæns


# Man kan også lave arrays i 2D, og trække værdier ud på samme måde,

# In[6]:


array5 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array5) #viser hele arrayet

print(array5[1,1]) #udskriver indeks (1,1)

print(array5[:,0]) #udskriver første kolonne i matricen

print(np.sum(array5,axis=0)) #bestemmer summen af kolonnerne


# En af grundene til at vi bruger NumPy arrays er, at vi nemt kan bruge NumPy funktioner til at lave regneoperationer på arrays. Her følger et par eksempler,

# In[7]:


tal = np.arange(0,10) #heltal fra 0 til 9

kvadrat = tal**2 + 1 #tager kvadratet plus 1 for alle tal i arrayet

Sinus = np.sin(tal) #tager sinus til alle tal i arrayet

#printer array, og de to resultater
print(tal)
print(kvadrat)
print(Sinus)


# ## Funktioner til statistik
# 
# Når vi laver databehandling i lab, skal vi ofte bruge gennemsnit og spredning på vores data, og det kan vi gøre nemt med et par NumPy funktioner. Arbejder man med 2D-datasæt, f.eks. ved gentagne målinger for skiftende variable, hvor vi vil have gennemsnittet for hver opstilling, skal man være opmærksom på at indikere akse i datasættet. Aksen sættes enten til 0 eller 1, afhængig af om man vil tage gennemsnittet lodret gennem kolonner eller vandret gennem rækker.

# In[9]:


data1 = np.array([3.2,4.1,3.7,4.3,3.3]) #indtaster et datasæt
gennemsnit1 = np.mean(data1) #tager gennemsnit
spredning1 = np.std(data1) #finder spredningen
print("Gennemsnit: ", gennemsnit1,"\nSpredning: ", spredning1) #\n sætter blot det efterfølgende printet på ny linje

data2 = np.array([[1,2,3], [1.2,1.9,3.2], [0.8,2.1,3.4]]) #indtaster et 2D datasæt
gennemsnit2 = np.mean(data2, axis = 0) #vi ønsker at tage gennemsnittet gennem kolonner. 
spredning2 = np.std(data2, axis = 0)

print("Det her er et 2D-array, \n", data2)
print("Gennemsnit: ",gennemsnit2, "\nSpredning: ", spredning2)


# ## Importering af datafiler
# Når vi arbejder i lab har vi ofte et måleinstrument der tager målingerne, så det både er mere præcist og man kan tage flere målinger hurtigt.
# Men når man gør det får man store mængder data og det gider vi ikke sidde og taste ind manuelt. Derfor vil vi bruge Python til det i stedet. For at gøre dette bruger vi igen NumPy pakken. Vi skal bruge kommandoen np.genfromtxt, syntaxen af denne er;
# 
# np.genfromtxt(fname, delimiter=None, skip_header=0, skip_footer=0) 
# 
# Hvor fname er fil navnet, delimiter er hvordan dataen er opdelt i filen (mere om det om lidt), skip_header er hvor mange linjer af toppen af filen der skal springes over og skip_footer er det samme bare fra bunden af. Dette er en forsimplet syntax den hele findes her hvis du gerne vil læse lidt mere [np.genfromtxt syntax](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html). Den måde '=0' skal forståes er at hvis du ikke skriver skip_header='noget' så antager Python at du mener 0.
# **Obs**: Det er vigtigt at data filen som hedder fname ligger i den samme mappe som koden. Så sørg for at gemme jeres Notebook og datafil i samme mappe.
# 
# Her følger et eksempel, med datafilen "Testdata.csv" der er uploadet på Absalon.

# In[10]:


data = np.genfromtxt('Testdata.csv', delimiter = ';', skip_header=2) #vores data er adskilt med semi-kolon, og vi springer 2 linjer over


print(data)


# Inden man importerer datafilen er det vigtigt at kigge lidt på filen først. Det gør I ved at åbne jeres datafil i jeres foretrukne filredigeringsprogram. Hent den fil der hedder Testdata.csv som er uploadet sammen med denne Notebook, for at kunne kigge lidt på den og forstå importeringen. Hvis du åbner Testdata.csv, så kan du se at der er noget tekst allerøverst, derfor sætter vi skip_header=2, da der er to linjer af tekst vi ikke vil have importeret i vores kode.
# Videre ser vi at tallene er adskilt med semikolon. Det betyder at vi skal sætte delimiter = ';'. Udover det ser vi at vi får et todimensionelt array af data. Vi vil i dette tilfælde helst have kolonnerne hver for sig. En kolonne kan importeres således,

# In[11]:


kolonne1 = data[:,0]
print(kolonne1)


# In[ ]:




