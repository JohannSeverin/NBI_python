#!/usr/bin/env python
# coding: utf-8

# # Hvad er Python? 
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

# ## Logik i Python 

# Når vi skriver kode, er vi ret ofte interesseret i, om et udtryk er sandt eller falsk for vide, hvordan vi skal eksekvere resten af koden. Til dette benytter vi boolean variable, som enten kan være ```True``` eller ```False```. Enten kan vi selv definerer en variabel som værende sand ved at skrive ```switch = True```, men oftere skal vi dog tjekke om noget er sandt. 
# 
# Når man benytter to lighedstegn ```==``` tjekker Python om udtrykkende på hver side er lig hinanden. Eksempelvis kan vi se om vores defineret værdi er lig med 10: _Bemærk denne forskel et lighedstegn definerer og to sammenligner:_

# In[15]:


i = 10 # Definer variabel
i == 10 # Sammenlign variabel med værdi


# In[16]:


i += 2 # Vi øger værdien med 2
i == 10 # Og sammenligner igen


# I det andet tilfælde har vi redefineret i til ```i = 12``` og udtrykket er altså ikke længere sandt. 

# Udover at benytte <code>==</code> kan vi benytte forskellige andre tegn til at danne udsagn, der kan være sande eller falske:
# - <code>&lt;</code> eller <code>&gt;</code> fortæller om en værdi er større eller mindre end en anden
# - <code>&lt;=</code> eller <code>&gt;=</code> er ligesom overstående men inkluderer også lig med
# - <code>!=</code> givet modsat tegn af <code>==</code>. Altså spørger om noget _er forskelligt fra_
# - <code>not</code> ændrer sandhedsværdien af et udtryk til det omvendte, eksempelvis er værdien af <code>not True</code> netop <code>False</code> og dermed er <code>not 1 == 2</code> sandt idet 1 og 2 jo ikke er ens.
# - <code>in</code> kan bruges til at spørge om et element er i en liste. Eksempelvis vil <code>7 in tal</code> give True i vores eksempel ovenfor.

# ## If-else-statements

# Særligt gøre boolean logik sig nyttig, når vi skal eksekvere noget kode, hvis et bestemt udtryk er sandt og noget andet, hvis det ikke er. Her kan vi benytte if/else statements. Her ser syntaksen sådan her ud: 
# ``` python
# if Statement:
#     gør det her
# else:
#     gør noget andet
# ```
# Hvad der sker, afhænger af sandhedsværdien af udtrykket "Statement" (altså om resultatet, der en en boolean, er <code>True</code> eller <code>False</code> ligesom i eksemplet med <code>i == 10</code> ovenfor). Hvis det logiske udsagn "Statement" er sandt, udføres første del af koden, ellers udføres den anden del. Man kan udelade <code>else</code>, og i dette tilfælde vil der kun ske noget såfremt "Statement" er sandt.
# Bemærk at indrykningen spiller en vigtig rolle i at afgrænse hvad der skal gøres i de enkele tilfælde.

# Her er et eksempel, hvor vi vil tage absolutværdien af et tal:

# In[12]:


a = -100
if a < 0: # Hvis a er negativt, så gør følgende:
    # Vi printer, hvis vi går ind i denne del af koden.
    print("Bingo: Vi startede med et negativt tal, så if-betingelsen var opfyldt") 
    a = - a   # Sæt a lig med sig selv med omvendt fortegn
print(a)


# Hvis vi gentager testen nu hvor a er blevet positiv, vil betingelsen i if-sætningen ikke være opfyldt, og der sker ikke noget i if-sætningen:

# In[13]:


if a < 0: # Hvis a er negativt, så gør følgende:
    print("Bingo: Vi startede med et negativt tal, så if-betingelsen var opfyldt") # Vi printer, hvis vi går ind i denne del af koden.
    a = - a  
print(a)


# Bemærk at <code>print(a)</code> ikke er indrykket og dermed ikke er en del af if-sætningen. Værdien af a udskrives derfor uanset fortegn.

# Hvis vi nu ønsker at dividere et tal med et andet, men returne den tomme variabel <code>None</code>, hvis vi bliver bedt om at dividere med 0 (og dermed undgår en fejlmeddelelse),  kan vi benytte vores if-else:

# In[1]:


tæller = 10
nævner = 0

if nævner != 0: # Hvis nævneren er forskellige fra nul, kan brøken beregnes
    resultat = tæller / nævner
else: # Ellers kan vi ikke beregne resultatet
    resultat = None   # None er et tomt element. Denne har ingen værdi

print(resultat)


# Hvis der er brug for flere rangordnede betingelser for at afgøre hvilken handling, koden skal udføre, kan man benytte <code>elif second_statement</code> (elif er kort for else-if). Så opbygger man syntaksen som
# ``` python
# if Statement:
#     gør det her
# elif Second_statement:
#     gør en andet ting
# else:
#     ellers gør det her
# ```
# Hvis man vil tjekke flere ting, kan man blot tilføje flere <code>elif</code> statements under hinanden.  
# I dette tilfælde vil koden altid køre præcis én kodebid: Koden checker først "Statement", og hvis denne er sand vil den __kun__ køre den tilhørende del af koden uanset om "Second_statement" også er sand. Ellers vil den tjekke <code>elif</code>-statementerne i rækkefølge. Hvis ingen af de givne betingelser er opfyldt, vil den køre koden der følger efter <code>else</code>.

# ## Løkker/loops

# Ofte bruger vi computeren til at gentage opgaver mange gange. Dette gør vi ved brug af løkker, som ofte kaldes loops. Der er to typer: en <code>for</code>-løkke og en <code>while</code>-løkke, i denne Notebook vil vi dog kun vise for-løkker, som benyttes som:
# ```python
# for variabel in liste:
#     Gør det her
# ```
# Løkken tildeler den variable værdier fra listen (i listens rækkefølge) og gør for denne værdi hvad det indrykkede stykke kodetekst specificerer. Det er normal praksis at kalde den variable i løkke-definitionen for <code>i</code> hvis der ikke er nogen særlig grund til at bruge et andet navn. Hvis vi eksempelvis vil beregne og udskrive kvadratet på 2, 3, 5 og 7, kan vi skrive det som:

# In[45]:


tal = [2, 3, 5, 7]

for i in tal: # Den variable hedder 'i' og vil antage værdierne i listen 'tal'.
    print(i ** 2) # Print tallet i anden


# Hvis vi er interreseret i at gøre noget et bestemt antal gange, kan vi benytte <code>range(antal)</code> til at generere en liste med tallene fra <code>0</code> og op til <code>antal - 1</code> (på grund af nulindekseringen så er der stadig 'antal' tal i listen). Lad os prøve at gange et tal med 10 og printe det 5 gange:

# In[21]:


a = 3
for i in range(5): # Vi har denne gang ikke tænkt os at benytte 'i' til noget, men det skal stadig være der
    a *= 10 # redefiner a ved at gange det med 10
    print(a)


# Vi kan også give <code>range()</code> flere argumenter. Kaldesekvensen er <code>range(start, stop, skridtstørrelse)</code> hvor alle tallene er heltal. Det er vigtigt at notere sig, at værdien 'stop' ikke kommer med i listen, så hvis vi ønsker at finde summen af alle tal i 5-tabellen fra 0 til 40, kan vi skrive:

# In[56]:


summen = 0
for i in range(0, 45, 5): # For at nå op til 40 skal 'range' have et helt tal mellem 41 og 45 som værdien for 'stop'
    print(f"Vi lægger {i} til {summen}")
    summen += i
    
print(f"Og summen er {summen}")


# Vi havde fået samme resultat, hvis vi i stedet for 45 havde skrevet 41, da range forsætter ind til i'et er større eller lig med vores <code>stop</code>.
