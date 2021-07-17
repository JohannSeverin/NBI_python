#!/usr/bin/env python
# coding: utf-8

# # Kom i gang med Python
# I løbet af de første halve år på jeres uddannelse i fysik, kommer I til at bruge python både i MekRel og i LinAlys. Der er mange forskellige måder at skrive python på, men vi vil foreslå, at I benytter Jupyter Notebook i en installation af Anaconda, da denne indeholder alt, hvad man umiddelbart skal bruge.
# 
# I Notebooks skriver man sin kode i celler. I vil typsik bruge celler i Code eller Markdown format. Dette er en Markdown celle og indholdet formatteres som tekst når cellen køres. Code celler er de celler vi skriver vores kode i. Markdown celler kan i evt. bruge til at skrive noter i, hvis der er noget om koden der er lidt kompliceret eller vigtigt at huske ift. jeres forsøg. Man kan med fordel bruge tastaturgenvejen `shift` + `enter` for at køre en celle, og bevæge sig videre til den næste i rækken.
# 
# Derudover er det vigtigt at understrege at i **ikke** skal bruge Notebooks som logbøger til labafleveringer. Logbøger eller rapporter skal ikke indeholde kode, kun resultatet af jeres kode (ex. plots, resultater), og kan med fordel skrives i Word, LaTeX el.lign. og **skal** afleveres i .pdf-format. Senere i kurset vil i blive stillet særlige opgaver i Python i form af såkaldt Pythonafleveringer, nogle af disse __må__ *godt* afleveres som Notebooks, men det hører i mere om senere.

# ## Hvordan virker Python?
# 
# Når  vi skriver kode i en celle og kører det, så bliver det læst linje for linje. Man koger derfor ens opgave ned i små dele, som kan bliver udført i træk. Alt hvad der står efter et <code>#</code> i koden bliver dog ikke læst, og dette skal forstås, som at det er en kommentar til den, der læser koden.
# 
# Når man arbejder i python, gemmes svaret på en operation ikke nødvendigvis. Vi benytter derfor <code> = </code> til at definerer en variabel. Dette kunne eksempelvis være <code> a = 5 </code>, så vil vi kunne indsætte <code>a</code> i et udtryk, og <code>a</code> vil nu blive betragtet som <code>5</code>.
# 
# En god måde at se en værdi på, er ved at bede Python om at printe den, dette gøres ved at skrive <code>print(X)</code>, hvor X kan være et hvilket som helst variabelnavn.
# 
# Eksempelvis kan vi definere variablen <code>hello</code> og printe den. 

# In[1]:


hello = "Hello World" # Anførselstegnene (eller "gåseøjnene") indikerer at variablen tildeles et tekstudtryk, en såkaldt "string"
print(hello)


# I en notebook er det faktisk ikke nødvendigt at printe den sidste linje, man kan blot skrive variabelnavnet, og så vil Jupyter selv printe det: 

# In[2]:


hello


# ### Variabel typer
# 
# Udover tekststrenge, som vi så i overstående eksempel, findes flere forskellige typer variable, som man kan benytte sig af. I Python er det dog ikke nødvendigt at angive disse, da sproget selv finder ud af det fra kontekst.
# 
# De mest almindelige variable typer er: 
# - Integers (heltal): her skriver vi blot et helt tal, som eksempelvis <code>a = 6</code>
# - Float (decimaltal): indgår der et decimalpunktum, '.', får vi automatisk en float variabel, som eksempelvis <code> pi = 3.14</code>. Bemærk at <code>a = 6</code> og <code>a = 6.</code> derfor ikke er det samme, selvom værdien er det.
# - String (tekststræng): Når vi vil have en variabel til at indeholde tekst, markeres det med anførselstegn/gåseøjne, f.eks. som ovenfor <code> hello = "Hello World"</code>
# - Boolean (sandt/falsk): Hvis vi skal angive en værdi som enten sand eller falsk, bruger vi en "boolean variable" og skriver <code>switch = True</code>. Falsk skal gives ved <code>False</code>, og bemærk igen at der er forskel på <code>Svar = True</code> og <code>Svar = "True"</code>, idet <code>Svar</code> i sidstnævnte tilfælde istedet bliver en string indeholdende ordet True, og ikke et logisk udtryk.
# 
# ### Lister af variable 
# 
# Vi kan sammensætte lister af flere værdier, eksempelvis en samling af tal. Dette gøres mest almindeligt ved at lave en liste.:
# <code>tal = [4, 7, 10]</code>. Nu vil <code>tal</code> altså indeholde værdierne 4, 7 og 10. Hvis vi ønsker et enkelt element fra vores liste kan vi hente dem ved at skrive <code>tal[index]</code>, hvor værdien af index angiver placeringen i listen vi ønsker at få ud. __Bemærk at Python starter ved nul (nul-indeksering), så det første element er altså <code>tal[0]</code>.__

# In[4]:


tal = [4, 7, 10]
tal[1]


# Vi ser altså, at når vi kalder <code>tal[1]</code> får vi det andet element ud, som i definitionen var givet ved 7. Dette er et resultat af nul-indeksering, og er noget, der ofte kan give fejl indtil man vænner sig til Python, så tjek det, hvis koden ikke virker eller giver uventede resultater.

# Vi kan tilføje et element til listen ved at benytte notationen <code>.append(element)</code>. Dette tilføjer elementet til den pågældende variabel i slutningen af listen. Eksempelvis, hvis vi ønsker at udvide vores tal-liste, kan vi skrive:

# In[5]:


tal.append(6)
tal


# Og vi har nu tilføjet 6 til vores liste. 

# ## Basale regneoperationer

# Python indeholder som udgangspunkt de mest basale regne-operationer, som man kender fra sin lommeregner. Eksempelvis kan vi lægge til, trække fra, gange og divdere ved blot at skrive udtrykket op med '+', '-', '*' og '/'. På sædvanligvis  kan vi også benytte parenteser til at give rækkefølgen for operationerne. Nogle enkelte eksempler er givet nedenunder:

# In[21]:


# Vi adderer blot to tal
2 + 2


# In[22]:


# Angiver vi ikke parenteser, følger Python selv regne-hierakiet
9 - 3 * 2


# In[5]:


# Men vi kan selvfølgelig ændre dette med parenteser
(9 - 3) * 2


# In[23]:


# Og vi skal selvfølgelig ikke dividere med 0, hvis ikke vi ønsker en fejl
100 / 0


# Udover disse operationer, kan vi også opløfte i en potens ved at benytte <code>**</code>.

# In[26]:


print(17 ** 2) # Kvadratet på 17

print(81 ** (1/2)) # Eller benytte at kvadratroden af x er x**(1/2) til at finde kvadratroden af 81


# In[27]:


print(81 ** 1/2) # Bemærk at dette IKKE beregner kvadratroden af 81 ligesom ovenfor:forskellen er parentesen


# Ønsker man at benytte funktioner som logaritmer, trigonometriske funktioner eller lign., bliver man ofte nødt til at importere et modul, som kan gøre det. Men det vil vi komme ind på senere.

# ### Ændring af variable

# Der kan være mange årsager til, at man skal ændre værdien på en varibel, det kunne f. eks. være i en simulation, hvor positionen skal opdateres. Sætter vi variabel navnet lig med en ny værdi ændres dette blot:

# In[12]:


vari = 15
print(vari) # Her er variablen lig med 15
vari = 20 
print(vari) # Nu er den sat til 20


# Når vi benytter et lighedstegn, så udregnes først værdien på højre side, inden værdien bliver gemt med variabelnavnet til venstre. Vi kan altså godt benytte en variabel til at redefinerer sig selv. Her benytter vi vari til at gøre vari 10 gange større.

# In[33]:


vari = 7
print(vari) # Sat til 7
vari = 10 * vari # vari bruges til at udregne en ny værdi for sig selv
print(vari)


# Der er dog også nogle indbyggede smutveje til at ændre variables værdier i faste trin. Hvis man gere vil lade en variabel vokse i skridt af <code>increment = 2.5</code>, kan man benytte smutvejs-notationen <code>+=</code> til at ændre variablen i skridt af <code>increment</code>

# In[34]:


increment = 2.5
value = 5
print(value)

value += increment # Vi øger value med værdien af vores increment
print(value)


# Dette virker også for de andre basale operationer ved at skrive <code>-=, *=</code>, og man kan eksempelvis benytte <code>/= 2</code>, til at redefinere et tal til at være halvt så stort. 
# 
