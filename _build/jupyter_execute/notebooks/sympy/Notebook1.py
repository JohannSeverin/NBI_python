#!/usr/bin/env python
# coding: utf-8

# __Foreslået ændringer__  
# Denne note book bliver skrevet om til et fælles dokument med MekRel
# 
# Se derfor ændringer under _introduktion til python_. 
# 
# Overordnet er dokumentet kogt ned, så den blot indeholder det mest vigtige. Da det er skrevet sammen med MekRel har vi valgt stadig at beholde if/else statements og løkker, da de også er vigtige for en programmerings tankegang. 
# 

# # Python i LinAlys
# 
# LinALys-kurset indeholder to spor (analyse og lineær algebra) og har fokus på "blyantsregning" og forståelse af den bagvedliggende teori. Ind imellem får vi brug for et værktøj til at tegne funktioner og foretage både numeriske og symbolske beregninger for at illustrere en problemstilling og/eller støtte eller kontrollere beregningerne i hånden. I år har vi valgt at bruge Python-modulet SymPy som CAS-værktøj (Computer Algebra System). Python og SymPy er ikke nødvendigvis det optimale værktøj til alle de opgaver, vi løser med Python i kurset, men vi har valgt Python fordi det er standardprogrammeringssproget på fysikstudiets førstedel, så de kræfter, du kommer til at bruge på Python, får du forhåbentlig gavn af andre steder (f.eks. i MekRel-kurset). Dette dokument er det første af en række notebooks, der introducerer de nødvendige koncepter.
# 
# Det er vigtigt at være opmærksom på, at modsat CAS-værktøjer som Maple, TI_Nspire og WordMat, så er Python ikke lavet specifikt til symbolske udregninger, men er et generelt anvendeligt programmeringssprog. Man skal derfor vænne sig til både Pythons syntaks og programmering som helhed for at få det maksimale ud af SymPy. Når det til gengæld er klaret, er det muligt at benytte SymPy i en lang række sammenhænge, og f.eks. nemt skifte mellem numeriske og symbolske anvendelser. Dette vil vi vende tilbage til, når vi har forudsætningerne på plads.
# 
# Dette er ikke en grundig indføring i Python, men vi vil i stedet med eksempler vise hvordan man benytter SymPy til at løse typiske opgaver og tegne funktioner. I nogle tilfælde stilles der i kurset opgaver, hvor man skal arbejde  videre med disse eksempler. Hvis man ønsker en dybere forståelse for Python, kan vi anbefale det online (gratis) kursus i Python på https://www.kaggle.com/learn/python, hvorefter man kan prøve kræfter med nogle udfordringer på https://projecteuler.net/.
# 
# ___Studerende, der allerede er bekendt med Python anbefales at springe let hen over teksterne men at kigge kode-eksemplerne igennem for at bekræfte, at man har forstået dem.___

# ## Hvordan virker en Jupyter notebook?

# I en Notebook skriver man Python-kode i forskellige celler (felter), og man kører derefter koden i den celle, man befinder sig i. Koden bliver læst linje fra linje i den enkelte celle fra top til bund, og efter cellens kode er blivet kørt, vil notebooken huske de variable man har indlæst, og man kan forsætte med kode, der bruger disse variable i en celle længere nede. Hvis man ønsker at køre en enkelt celle, er det smart at benytte genvejen <code>shift</code> + <code>enter</code>.
# 
# Felterne i en notebook kommer i to typer: markdowns og kode. Det felt, du læser nu, er eksempelvis et Markdowns-felt, hvor resultatet er formatteret tekst. Derudover er der kodefelter, som vi vil se snart, hvor vi skriver selve koden og kan køre/afvikle den. 

# ## I Python er alt en variabel
# Noget, som man skal vende sig til i Python er, at alt er variable. Det vil sige, at hvis vi skriver <code> a = 5 </code>, så vil vi kunne indsætte <code>a</code> i et udtryk, som så vil returnere <code>5</code>.
# 
# En god måde at se en værdi på, er ved at bede Python om at printe den, dette gøres ved at skrive <code>print(X)</code>, hvor X kan være et hvilket som helst variabelnavn.
# 
# Eksempelvis kan vi definere variablen <code>hello</code> og printe den. 
# _Længere forklaringer vil oftest stå i et Markdowns-felt, mens vi makerer kommentarer inde i koden med et hashtag #. Hvis en linje starter med #, bliver det ikke læst og afviklet som kode_

# In[11]:


hello = "Hello World" # Anførselstegnene (eller "gåseøjnene") indikerer at variablen tildeles et tekstudtryk, en såkaldt "string"
print(hello)


# Vi ser altså, at konsollen returnerer <i>Hello World</i>, der er værdien af den variable <code>hello</code>.
# 
# De forskellige typer af variable, som vi oftest vil møde, er:
# - Integers (heltal): her skriver vi blot et helt tal, som eksempelvis <code>a = 6</code>
# - Float (decimaltal): indgår der et decimalpunktum, '.', får vi automatisk en float variabel, som eksempelvis <code> pi = 3.14</code>. Bemærk at <code>a = 6</code> og <code>a = 6.</code> derfor ikke er det samme, selvom værdien er det.
# - String (tekststræng): Når vi vil have en variabel til at indeholde tekst, markeres det med anførselstegn/gåseøjne, f.eks. som ovenfor <code> hello = "Hello World"</code>
# - Boolean (sandt/falsk): Hvis vi skal angive en værdi som enten sand eller falsk, bruger vi en "boolean variable" og skriver <code>switch = True</code>. Falsk skal gives ved <code>False</code>, og bemærk igen at der er forskel på <code>Svar = True</code> og <code>Svar = "True"</code>, idet <code>Svar</code> i sidstnævnte tilfælde istedet bliver en string indeholdende ordet True, og ikke et logisk udtryk.
# 
# Vi kan sammensætte lister af flere værdier, eksempelvis en samling af tal. Dette gøres mest almindeligt ved at lave en liste.:
# <code>tal = [4, 7, 10]</code>. Nu vil <code>tal</code> altså indeholde værdierne 4, 7 og 10. Hvis vi ønsker et enkelt element fra vores liste kan vi hente dem ved at skrive <code>tal[index]</code>, hvor værdien af index angiver placeringen i listen vi ønsker at få ud. __Bemærk at Python starter ved nul (nul-indeksering), så det første element er altså <code>tal[0]</code>.__
# Eksempel:

# In[19]:


tal = [4, 7, 10]
tal[1]


# _Vi benytter her at Jupyter Notebook printer det sidste element, vi har beregnet. Altså kan vi i den nederste linje i en celle undlade at skrive <code>print(...)</code> for at se resultatet af beregningen. Vi skal dog fortsat bruge <code>print(...)</code> hvis vi vil have en mellemregning printet. Hvis vi gerne vil undgå at få udskrevet sidste linje, tilføjes et semikolon._  
# Vi ser altså, at når vi kalder <code>tal[1]</code> får vi det andet element ud, som i definitionen var givet ved 7. Dette er et resultat af nul-indeksering, og er noget, der ofte kan give fejl indtil man vænner sig til Python, så tjek det, hvis koden ikke virker eller giver uventede resultater.  
# Vi vil introducere andre typer af lister senere hvis de bliver nødvendige.

# Vi kan tilføje et element til listen ved at benytte notationen <code>.append(element)</code>. Dette tilføjer elementet til den pågældende variabel i slutningen af listen. Eksempelvis, hvis vi ønsker at udvide vores tal-liste, kan vi skrive:

# In[20]:


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


# Man kan også komme ud for at skulle bruge integer-division: <code>//</code> eller modulo <code>%</code>. Som kan opfattes som hhv. division med efterfølgende nedrunding til nærmeste helttal og at bestemme resten af en division. Eksempelvis, hvis vi ønsker at kende den heltallige division og resten af 100 med 11, regnes det som:  
# _Jeg har her benyttet tekst-formatering, læs eventuelt [note om formatering her](https://realpython.com/python-f-strings/)_

# In[28]:


division = 100 // 11    # // for integer-division
rest = 100 % 11         # %  for rest

# Vi printer nu ved at formatere strængen, så vi indsætter værdierne, der hvor det giver mening at se dem.
print(f"100 delt med 11 giver {division} med en rest på {rest}")


# Ønsker man andre funktioner som logaritmer, eksponentialfunktioner, trigonometriske funktioner eller lignende importere man dem oftest fra et modul. Python har et indbygget Math modul, som man tit kan bruge. Hvis man for eksempel skal lave trigonometriske funktioner,  skriver man <code>from math import cos, sin, tan</code>, og man kan da bruge funktionerne blot ved at bruge <code>cos(x)</code>. I praksis bruger man sjældent math-modulet og bruger i stedet enten NumPy, som vil blive brugt i MekRel-lab til numeriske beregninger, eller som her SymPy, som indeholde disse funktioner som symbolske udtryk. Herunder er vist eksempler:
# 

# In[9]:


from math import cos
cos(3.14 / 6)


# In[10]:


from numpy import cos
cos(3.14/6)


# In[32]:


from sympy import cos
cos(3.14/6)


# ### Redefinering af variable

# Ret ofte er det smart at kunne opdatere en variabel med en ny værdi, f.eks når man laver en simulation hvor f.eks. stedkoordinaterne ændres som tiden går. For at opdatere en variabel overskriver man den bare med en ny:

# In[12]:


vari = 15
print(vari) # Her er variablen lig med 15
vari = 20 
print(vari) # Nu er den sat til 20


# Man kan også bruge en variabel til at redefinere sig selv. Eksempelvis, hvis man ønsker at gange sin variabel med 10.

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

# ## Lighedstegnets dobbelte betydning

# Når vi tildeler en variabel en værdi, bruger vi - som vi viste det ovenfor - et almindeligt lighedstegn. Er vi derimod interesserede i at undersøge om en variabel har en bestemt værdi (eller om to udtryk eller variable har den samme værdi), bruges to lighedstegn: vi skriver <code>if i == 10</code> og Python vil returnere <code>True</code> eller <code>False</code> afhængigt af værdien af i:

# In[15]:


i = 10 # Definer variabel
i == 10 # Sammenlign variabel med værdi


# In[16]:


i += 2 # Vi øger værdien med 2
i == 10 # Og sammenligner igen


# ## If-else-statements

# Når man skriver sin kode, vil man ret ofte kun udfører bestemte dele af koden hvis nogle bestemte betingelser er opfyldt. Dette kan man gøre ved et if-else statement. Syntaksen ser ud som:   
# ``` python
# if Statement:
#     gør det her
# else:
#     gør noget andet
# ```
# Hvad der sker, afhænger af sandhedsværdien af udtrykket "Statement" (altså om resultatet, der en en boolean, er <code>True</code> eller <code>False</code> ligesom i eksemplet med <code>i == 10</code> ovenfor). Hvis det logiske udsagn "Statement" er sandt, udføres første del af koden, ellers udføres den anden del. Man kan udelade <code>else</code>, og i dette tilfælde vil der kun ske noget såfremt "Statement" er sandt.
# Bemærk at indrykningen spiller en vigtig rolle i at afgrænse hvad der skal gøres i de enkele tilfælde. Der bruges ikke "end" i forbindelse med if-sætninger i Python.

# Udover at benytte <code>==</code> kan vi benytte forskellige andre tegn til at danne udsagn, der kan være sande eller falske:
# - <code>&lt;</code> eller <code>&gt;</code> fortæller om en værdi er større eller mindre end en anden
# - <code>&lt;=</code> eller <code>&gt;=</code> er ligesom overstående men inkluderer også lig med
# - <code>!=</code> givet modsat tegn af <code>==</code>. Altså spørger om noget _er forskelligt fra_
# - <code>not</code> ændrer sandhedsværdien af et udtryk til det omvendte, eksempelvis er værdien af <code>not True</code> netop <code>False</code> og dermed er <code>not 1 == 2</code> sandt idet 1 og 2 jo ikke er ens.
# - <code>in</code> kan bruges til at spørge om et element er i en liste. Eksempelvis vil <code>7 in tal</code> give True i vores eksempel ovenfor.

# Her er et eksempel, hvor vi vil tage absolutværdien af et tal:

# In[40]:


a = -100
if a < 0: # Hvis a er negativt, så gør fælgende:
    print("Bingo: Vi startede med et negativt tal, så if-betingelsen var opfyldt") # Vi printer, hvis vi går ind i denne del af koden.
    a = - a   # Sæt a lig med sig selv med omvendt fortegn
print(a)


# Hvis vi gentager testen nu hvor a er blevet positiv, vil betingelsen i if-sætningen ikke være opfyldt, og der sker ikke noget i if-sætningen:

# In[58]:


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

# Ofte bruger vi computeren til at gentage opgaver mange gange. Dette gør vi ved brug af løkker, som ofte kaldes loops. Der er to typer: en <code>for</code>-løkke og en <code>while</code>-løkke. <code>For</code>-løkken benyttes som:
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


# Vi kan også give <code>range()</code> flere argumenter. Syntaksen er <code>range(start, stop, skridtstørrelse)</code> hvor alle tallene er heltal. Det er vigtigt at notere sig, at værdien 'stop' ikke kommer med i listen, så hvis vi ønsker at finde summen af alle tal i 5-tabellen fra 0 til 40, kan vi skrive:

# In[56]:


summen = 0
for i in range(0, 45, 5): # For at nå op til 40 skal 'range' have et helt tal mellem 41 og 45 som værdien for 'stop'
    print(f"Vi lægger {i} til {summen}")
    summen += i
    
print(f"Og summen er {summen}")


# Vi havde fået samme resultat, hvis vi i stedet for 45 havde skrevet 41, da range forsætter ind til i'et er større eller lig med vores <code>stop</code>. Det er til gengæld god skik, at sætte stop-argumentet til at være lig den værdi, som det næste skridt havde været. 

# Vores anden type løkke er <code>while</code>-løkker, som kører så længe, en given betingelse er opfyldt. Det betyder også, at programmet kan blive fanget i en uendelig løkke, så pas på med while-løkker! Syntaksen er:
# ```python
# while statement:
#     Gør noget
# ```
# Hvor statement, er et udtryk ligesom for <code>if</code>-statements (en boolean variabel).
# 
# Som eksempel vil vi bruge en <code>while</code>-løkke til at lave en beregning af n! for et tal n. Vi ganger n med n-1 som vi ganger med n-2 osv. indtil vi når 0, og er færdige:

# In[57]:


x = 7 # Vi vil finde 7 fakultet

# Vi definere foreløbigt resultatet som 1
resultat = 1 

while x > 0: # Løkken kører så længe x er over 0
    resultat *= x # multiplicér resultat med x
    x -= 1        # reducer x med 1

print(resultat)


# Når koden advikles, vil der ske følgende:
# - x defineres til 7
# - Den variable 'resultat' defineres til 1 (fordi 1! = 1)
# - Da x = 7, og 7 > 0 går vi ind i <code>while</code>-løkken
# - 'resultat' ganges med x og 'resultat' opdateres til den nye værdi. Vi får altså at 'resultat' er lig med 1 * 7
# - Vi trækker nu 1 fra x, så x er nu 6. 
# - Løkken er nu gennenløbet første gang, og vi starter igen
# - Da x = 6 er værdien af x således stadig over 0, og vi går igen ind i løkken
# - 'resultat' ganges med x og erstatter den tidligere værdi. Vi får at 'resultat' er lig med 7 * 6
# - Vi trækker en fra x og er færdig med andet gennemløb
# 
# Dette forsætter indtil x = 0, nu vil <code>x > 0</code> være <code>False</code>, og vil derfor ikke gå ind i løkken og i stedet fortsætte i koden, hvor vi printer vores resultat.

# Man kan eventuelt benytte et <code>break</code>-statement inde i en løkke for at bryde ud af løkken selvom betingelsen i løkken-definitionen stadig er opfyldt. Eksempelvis kan man skrive:
# ```python
# while statement:
#     do_something
#     if andet_statement:
#         break
# 
# ```
# Her vil vi altså bryde ud af vores <code>while</code>-løkke, hvis <code>andet_statement</code> viser sig at være sandt, da vi så vil kører koden <code>break</code>. Dette bruges ofte som en slags nødudgang hvis der opstår et uønsket resultat eller en nødvendig betingelse for at beregningen kan foretages ikke længere er opfyldt.

# ## Import af biblioteker/libaries

# Python kan i sig selv ret meget, men det er oftest en fordel at basere sine udregninger på funktioner, som nogen (ret kvikke kodehaj(er)) har skrevet og testet allerede. Disse er samlet i biblioteker. Når man har installeret Anaconda, er der inkluderet mange Python biblioteker som umiddelbart kan importeres i et Python-script eller notebook. I LinALys og MekRel vil vi ofte bruge biliotekerne Matplotlib.pyplot til at plotte, Numpy til numeriske beregninger og SymPy til symbolske beregninger.

# Der er forskellige måder at importere et bibliotek på. Hvis man bare vil importere et helt bibliotek benytter man simpelthen <code>import sympy</code> og så kan man benytte sympys funktioner ved at skrive f.eks. <code>sympy.cos</code>. Da det ofte er lidt bøvlet, kan man i stedet give SymPy et kælenavn. I materialet i LinALys betegner vi SymPy med <code>sp</code>, og alle følgende notebooks vil derfor starte med <code>import sympy as sp</code>. Herefter vil SymPys funktioner kunne anvendes ved f.eks. at skrive <code>sp.exp(x)</code>

# Endelig kan man importere enkelte funktioner fra et bibliotek. Hvis man eksempelvis vil have matrix-funktionen fra SymPy, kan man skrive: <code>from sympy import Matrix</code> (ligesom vi gjorde i eksemplet ovenfor, da vi benyttede cosinus fra forskellige biblioteker). I dette tilfælde vil man _ikke_ skulle skrive bibliotekets navn op, men blot f.eks. skrive <code>Matrix([[1, 2], [3, 4]])</code>. Man kan ovenikøbet give en enkelt funktion en forkortelse, hvis man skriver <code>from sympy import Matrix as M</code>, ville den tilsvarende funktion blot kaldes ved <code>M([[1, 2], [3, 4]])</code>.
