#!/usr/bin/env python
# coding: utf-8

# # Kontrolstrukturer og Løkker
# 
# _Denne side bygger ovenpå den tidligere, og omhandler hvordan man kan bygge kode op med brugen af kontrolstrukturer og løkker til eksempelvis at gentage kode. I MekRel og LinAlys benytter vi dog primært moduler, som tager sig af den logik og de løkker, som man skal bruge. Derfor er det ikke strengt nødvendigt at læse den her side, selvom det er nogle meget brugbare emner, der helt sikkert vil være med til at forbedre forståelsen for Python._

# ## Logik i Python 

# Når vi skriver programkode, er vi ret ofte interesseret i, om et udtryk er sandt eller falsk for vide, hvordan vi skal eksekvere resten af koden. Til dette benytter vi boolean variable, som enten kan være ```True``` eller ```False```. Enten kan vi selv definere en variabel som værende sand ved at skrive ```switch = True```, men oftere skal vi dog tjekke om noget er sandt. 
# 
# Når man benytter to lighedstegn ```==``` tjekker Python om udtrykkene på hver side er lig hinanden. Eksempelvis kan vi se om vores defineret værdi er lig med 10:
# 
#  _Bemærk denne forskel: Et lighedstegn definerer en variabel og to lighedstegn efter hinanden sammenligner to udtryk:_

# In[15]:


i = 10 # Definer variabel
i == 10 # Sammenlign variabel med værdi


# In[16]:


i += 2 # Vi øger værdien med 2
i == 10 # Og sammenligner igen


# I det andet tilfælde har vi redefineret `i` til ```i = 12``` og udtrykket "`i` er lig med 10" er altså ikke længere sandt. 

# Udover at benytte <code>==</code> kan vi benytte forskellige andre tegn til at danne udsagn, der kan være sande eller falske:
# - <code>&lt;</code> eller <code>&gt;</code> fortæller om en værdi er større eller mindre end en anden
# - <code>&lt;=</code> eller <code>&gt;=</code> er ligesom overstående men inkluderer også lig med
# - <code>!=</code> er det modsatte af <code>==</code>, altså _er forskelligt fra_, og svarer til det matematiske tegn $\neq$.
# - <code>not</code> ændrer sandhedsværdien af et udtryk til det omvendte, eksempelvis er værdien af <code>not True</code> netop <code>False</code> og dermed er <code>not 1 == 2</code> sandt idet 1 og 2 jo ikke er ens.
# - <code>in</code> kan bruges til at spørge om et element er i en liste. Eksempelvis vil <code>7 in tal</code> give `True`, hvis `tal` er en liste, som indeholder 7, som det gjorde på tidligere side.

# ## If-else-statements

# Boolean-logik er særligt nyttigt hvis vi skal udføre forskellige beregninger når et bestemt udtryk er sandt og noget andet, hvis det ikke er. Her kan vi benytte if/else statements. Her ser syntaksen sådan ud: 
# ``` python
# if Statement:
#     ~ gør det her ~
# else:
#     ~ gør noget andet ~
# ```
# Hvad der sker, afhænger af sandhedsværdien af udtrykket `Statement`. Hvis det logiske udsagn `Statement` er sandt, udføres første del af koden, ellers udføres den anden del. Man kan udelade <code>else</code>, og i dette tilfælde vil der kun ske noget såfremt `Statement` er sandt.
# Bemærk at indrykningen spiller en vigtig rolle i at afgrænse, hvad der skal gøres i de enkelte tilfælde.

# Her er et eksempel, hvor vi vil tage absolutværdien af et tal:

# In[12]:


a = -100
if a < 0: # Hvis a er negativt, så gør følgende:
    # Vi printer, hvis vi går ind i denne del af koden.
    print("Bingo: Vi startede med et negativt tal, så if-betingelsen var opfyldt") 
    a = - a   # Sæt a lig med sig selv med omvendt fortegn
print(a)


# Hvis vi gentager testen nu hvor a er blevet positiv, vil betingelsen i if-sætningen ikke være opfyldt, og der udføres ingen beregninger i if-sætningen:

# In[13]:


if a < 0: # Hvis a er negativt, så gør følgende:
     # Vi printer, hvis vi går ind i denne del af koden.
    print("Bingo: Vi startede med et negativt tal, så if-betingelsen var opfyldt")
    a = - a  
print(a)


# Bemærk at <code>print(a)</code> ikke er indrykket og dermed ikke er en del af if-sætningen. Værdien af a udskrives derfor uanset fortegn.

# Et andet eksempel kunne være, hvis vi ønsker at dividere et tal med et andet, men have den tomme variabel <code>None</code>, hvis vi bliver bedt om at dividere med 0 (og dermed undgår en fejlmeddelelse). Til dette kan vi benytte vores if-else:

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
#     ~ gør det her ~
# elif Second_statement:
#     ~ gør en andet ting ~
# else:
#     ~ ellers gør det her ~
# ```
# Hvis man vil tjekke flere ting, kan man blot tilføje flere <code>elif</code> statements under hinanden.  
# I dette tilfælde vil koden altid køre præcis én kodebid: Koden checker først `Statement` og hvis denne er sand vil den __kun__ køre den tilhørende del af koden uanset om `Second_statement` også er sand. Hvis `Statement` er falskt, vil den tjekke <code>elif</code>-statementerne i rækkefølge og eksekvere koden hørende til den første sande betingelse. Hvis ingen af de givne betingelser er opfyldt, vil den køre koden der følger efter <code>else</code>.

# ## Løkker/loops

# Ofte bruger vi computeren til at gentage opgaver mange gange. Dette kan vi gøre ved brug af løkker (ofte kaldet _loops_ ligesom på engelsk). Der er to typer: en <code>for</code>-løkke og en <code>while</code>-løkke. I denne Notebook vil vi dog kun vise for-løkker, som bruges ved at sætte følgende struktur op:
# ```python
# for variabel in liste:
#     ~ gør det her ~
# ```
# Løkken tildeler `variabel` værdier fra listen. Kodebiden, som er indrykket køres nu en gang for hvert element i listen, hvor `variabel` hver gang refererer til det næste element i listen. Det er normal praksis at kalde den variable i løkke-definitionen for <code>i</code> hvis der ikke er nogen særlig grund til at bruge et andet navn. Hvis vi eksempelvis vil beregne og udskrive kvadratet på 2, 3, 5 og 7, kan vi skrive det som:

# In[1]:


tal = [2, 3, 5, 7]

for i in tal:     # Variablen hedder 'i' og vil efter tur antage værdierne i listen 'tal'.
    print(i ** 2) # Print kvadratet på tallet `i`


# Hvis vi er interreseret i at gøre noget et bestemt antal gange, kan vi benytte <code>range(antal)</code> til at generere en liste med tallene fra <code>0</code> og op til <code>antal - 1</code> (på grund af nulindekseringen så er der `antal` tal i listen). Lad os prøve at gange et tal med 10, printe det og så gentage dette 5 gange:

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


# Vi havde fået samme resultat, hvis vi i stedet for 45 havde skrevet 41, da range forsætter indtil i'et er større eller lig med vores <code>stop</code>.

# In[ ]:




