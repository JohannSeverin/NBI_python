#!/usr/bin/env python
# coding: utf-8

# # Kom i gang med Python
# På fysik stifter I bekendtskab med Python i de to førsteårskurser MekRel og LinAlys. Der er mange forskellige måder at skrive Python på, men vi vil foreslå, at I benytter Jupyter Notebooks, som kan findes i en installation af Anaconda. 
# 
# I Notebooks skriver man sin kode i celler, som derefter kan "køres". Der bliver primært brugt to slags celler: "Code" eller "Markdown". Denne celle er en Markdown-celle og indholdet formateres som tekst, når cellen køres (der laves altså ingen beregninger). Markdown-celler kan bruges til at skrive noter i: det kunne være ens overvejelser i forbindelse med et forsøg i laboratoriet eller en forklaring af tankegangen bag en beregning.
# Kodeceller er de celler, der indeholder de kommandoer, der laver vores beregninger når cellen køres.
# 
# **Tip:** Man kan med fordel bruge tastaturgenvejen `shift` + `enter` for at køre en celle, og bevæge sig videre til den næste celle i rækken.
# 

# ## Hvordan virker Python?
# 
# Når  vi skriver kode i en celle og kører cellen, bliver koden læst linje for linje. Et computerprogram bliver altså en liste af computer-operationer, som skal foretages i en bestemt rækkefølge. Hvis man vil markere noget, som comptueren ikke skal køre, kan det markeres med <code>#</code>. Dette bruges ofte til kommentar til den, der læser koden.
# 
# Når man arbejder i Python, gemmes svaret på en operation ikke nødvendigvis. Vi benytter derfor <code> = </code> til at definere en variabel. Dette kunne eksempelvis være <code> a = 5 </code>. Da vil vi kunne indsætte <code>a</code> i et udtryk, og <code>a</code> vil nu have værdien <code>5</code>.
# 
# En god måde at se en værdi på, er ved at bede Python om at printe den. Dette gøres ved at skrive <code>print(X)</code>, hvor X kan være et hvilket som helst variabelnavn.
# 
# Eksempelvis kan vi definere variablen <code>hilsen</code> og printe den. 

# In[2]:


hilsen = "Hello World" # Anførselstegnene (eller "gåseøjnene") indikerer at variablen tildeles et tekstudtryk, en såkaldt "string"
print(hilsen)


# I en notebook er det faktisk ikke nødvendigt at printe den *sidste* linje, man kan blot skrive variabelnavnet, og så vil Jupyter selv printe det: 

# In[4]:


hilsen


# ### Variabeltyper
# 
# Udover tekststrenge, som vi så i ovenstående eksempel, findes flere forskellige typer variable, som man kan benytte sig af. I Python er det ikke nødvendigt at angive typen af en variabel, da Python selv finder ud af det fra konteksten.
# 
# De mest almindelige variabeltyper er: 
# - Integers (heltal): her skriver vi blot et helt tal, som eksempelvis <code>a = 6</code>
# - Float (decimaltal): indgår der et decimalpunktum, '.', får vi automatisk en float-variabel, som eksempelvis <code>kroner_per_euro = 7.46</code>.
# - String (tekststreng): Når vi vil have en variabel til at indeholde tekst, markeres det med anførselstegn/gåseøjne, f.eks. som ovenfor <code>hilsen = "Hello World"</code>
# - Boolean (sandt/falsk): Hvis vi skal angive en værdi som enten sandt eller falsk, bruger vi en "boolean variable" og kan skrive <code>switch = True</code>. Falsk skal gives ved <code>False</code>, og bemærk igen at der er forskel på <code>Svar = True</code> og <code>Svar = "True"</code>, idet <code>Svar</code> i sidstnævnte tilfælde istedet bliver en string, som indeholder ordet True, og ikke et logisk udtryk.
# 
# ### Lister af variable 
# Vi kan sammensætte lister af flere værdier, eksempelvis en samling af tal. Dette gøres mest almindeligt ved at lave en liste.:
# <code>tal = [4, 7, 10]</code>. Nu vil <code>tal</code> altså indeholde værdierne 4, 7 og 10. Hvis vi ønsker et enkelt element fra vores liste, kan vi referere til det ved at skrive <code>tal[index]</code>, hvor værdien af index angiver placeringen i listen af det ønskede tal. 
# 
# **Tip:** Python starter ved nul (nul-indeksering), så det første element er altså <code>tal[0]</code>.

# In[5]:


tal = [4, 7, 10]
tal[1]


# Vi ser altså, at når vi kalder <code>tal[1]</code> får vi det andet element ud, som i definitionen var givet ved 7. Dette er et resultat af nul-indeksering. Dette er en hyppig kilde til fejl, når man ikke er vant til Python, så tjek det, hvis koden ikke virker eller giver uventede resultater.

# Elementer kan tilføjes til listen ved at benytte koden <code>.append(element)</code> efter vores liste. Dette tilføjer elementet til den pågældende variabel i slutningen af listen. Eksempelvis, hvis vi ønsker at udvide vores tal-liste, kan vi skrive:

# In[5]:


tal.append(6)
tal


# og vi har nu tilføjet 6 som et ekstra element i vores liste. 

# ## Basale regneoperationer

# Python indeholder som udgangspunkt de mest basale regneoperationer, som man kender fra sin lommeregner. Eksempelvis kan vi lægge til, trække fra, gange og dividere ved blot at skrive udtrykket op med '+', '-', '*' og '/'. På sædvanlig vis kan vi også benytte parenteser til at give rækkefølgen for operationerne. Nogle enkelte eksempler er givet nedenunder:

# In[6]:


# Vi adderer blot to tal
2 + 2


# In[7]:


# Angiver vi ikke parenteser, følger Python selv regne-hierakiet
9 - 3 * 2


# In[8]:


# Men vi kan selvfølgelig ændre dette med parenteser
(9 - 3) * 2


# In[9]:


# Og vi skal selvfølgelig ikke dividere med 0, hvis ikke vi ønsker en fejl
100 / 0


# Udover disse operationer, kan vi også opløfte i en potens ved at benytte <code>**</code>.

# In[26]:


print(17 ** 2) # Kvadratet på 17

print(81 ** (1/2)) # Eller benytte at kvadratroden af x er x**(1/2) til at finde kvadratroden af 81


# In[10]:


print(81 ** 1/2) # Bemærk at dette IKKE beregner kvadratroden af 81 ligesom ovenfor: forskellen er parentesen.


# Ønsker man at benytte funktioner som logaritmer, trigonometriske funktioner eller lignende, bliver man ofte nødt til at importere et modul, som kan indeholder disse funktioner. Men det vil vi komme ind på senere i noterne om SymPy og NumPy.

# ### Ændring af variable

# Der kan være mange årsager til, at man skal ændre værdien på en varibel. Det kunne f. eks. være i en simulation, hvor positionen af et objekt skal opdateres efter et lille tidsskridt. Benytter vi samme variabelnavn i en ny definition ændrer vi blot værdien:

# In[12]:


vari = 15
print(vari) # Her er variablen lig med 15
vari = 20 
print(vari) # Nu er den sat til 20


# Når vi benytter et lighedstegn, så udregnes først værdien på højre side, inden værdien bliver gemt med variabelnavnet til venstre. Vi kan altså godt benytte en variabel til at redefinere sig selv. Her benytter vi `vari` til at gøre `vari` 10 gange større.

# In[12]:


vari = 7
print(vari)      # Sat til 7
vari = 10 * vari # `vari` bruges til at udregne en ny værdi for samme variabel
print(vari)


# Der er dog også nogle indbyggede smutveje til at ændre værdien af variable i faste trin. Hvis man gerne vil lade en variabel vokse i skridt af <code>increment = 2.5</code>, kan man benytte smutvejs-notationen <code>+=</code> til at ændre variablen i skridt af <code>increment</code>

# In[34]:


increment = 2.5
value = 5
print(value)

value += increment # Vi øger value med værdien af den variable increment
print(value)


# Dette virker også for de andre basale operationer ved at skrive <code>-=, *=</code>, og man kan eksempelvis benytte <code>/= 2</code>, til at redefinere et tal til at være halvt så stort.

# In[ ]:




