#!/usr/bin/env python
# coding: utf-8

# # Matplotlib
# 
# Vi vil ofte i lab gerne formidle vores data i form af en figur. For at lave figurer bruger vi pakken Matplotlib.
# 
# Matplotlib er et kæmpe bibliotek og kan rigtig rigtig meget. Det er faktisk så stort at du kun skal bruge en lille del af det `pyplot`. Derfor skriver man `matplotlib.pyplot`, det svarer lidt til kun at læse bøgerne i fysikafdelingen af et bibliotek. 
# 
# Man skal også passe på, når man laver plots med matplotlib. Det mixer dårligt med `Sympy`, da matplotlib laver plots ud fra tal og ikke analytiske udtryk, som er det Sympy giver. Hvis man skal lave et plot med Sympy så kig i noten om Sympy.
# 
# 

# ## Plots
# 
# For at lave et plot skal vi først have data at arbejde med.
# 

# In[2]:


import numpy as np
xData = np.array([1,2,3,4])
yData = np.array([1,1.8,3.3,3.7])


# Når man laver et plot med Matplotlib bygger man det op trinvis. Først laves plottet ud af data med `plt.plot`. Derefter bygges aksenavne og en legend på. Et eksempel ses her,

# In[6]:


import matplotlib.pyplot as plt

plt.plot(xData, yData, 'o', label = "Data") #Vi plotter xData mod yData som store prikker, og giver datasættet en titel

plt.xlabel('Længde [cm]', fontsize = 20) #Tilføjer etiketter på akserne og angiver skriftstørrelse
plt.ylabel('Masse [g]', fontsize = 20)

plt.legend(fontsize = 13) #plotter en "legend", navnet hentes fra label i plt.plot

plt.savefig("figure.png") #gemmer figuren som en .png fil

plt.show() #viser figuren under den kørte celle


# I behøver ikke nødvendigvis manuelt indstille skriftstørrelsen på akser og legend hver gang, men det kan nogle gange være nødvendigt at justere, afhængig af hvor meget figurerne skal fylde i jeres logbog. Regelen er at man altid skal kunne læse akse-titlerne uden at zoome ind eller hive forstørrelsesglas frem. Vær også opmærksom på, at når I bruger funktionen plt.savefig(), gemmes jeres figur i samme mappe som jeres Notebook ligger, medmindre I indstiller det anderledes.
# 
# Det kan også være smart at ændre hvad der er på akserne, et eksempel med radianer ses under.

# In[7]:


#flere eksempler på at plotte

xVærdi = np.linspace(0,2*np.pi,100) #laver et array af værdierne fra 0 til pi, fordelt over 100 datapunkter

#bruger NumPy funktioner til at plotte sinus og cosinus til vores x værdier, og indikerer at punkter skal være en 
#prikket linje
plt.plot(xVærdi, np.sin(xVærdi), ':', label = "f(x) = sin(x)") 
plt.plot(xVærdi, np.cos(xVærdi), ':', label = "f(x) = cos(x)")

plt.xlabel('x') #sætter titler på akserne
plt.ylabel('f(x)')

# Følgende skridt er lidt unødvendigt, men plotter man ex. trigonometriske funktioner kan det være fedt at indstille
# aksen så værdierne "giver mening" ift. funktionen.
# Her indikerer første array hvor på x-aksen man vil have "ticks", og dernæst et array med hvad der skal stå på hvert
# "tick"
plt.xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi], ['0','$\pi/2$','$\pi$','$3/2\pi$','$2\pi$'])

plt.legend()

plt.show()


# Det er en masse forskelige andre ting man kan med at plotte men dette bør være nok til det I skal her.
