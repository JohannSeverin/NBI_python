#!/usr/bin/env python
# coding: utf-8

# # Python i LinAlys
# 
# LinALys-kurset indeholder to spor (analyse og lineær algebra) og har fokus på "blyantsregning" og forståelse af den bagvedliggende teori. Ind imellem får vi brug for et værktøj til at tegne funktioner og foretage både numeriske og symbolske beregninger for at illustrere en problemstilling og/eller støtte eller kontrollere beregningerne i hånden. I dette kursus har vi valgt at bruge Python-modulet SymPy som CAS-værktøj (Computer Algebra System). Python og SymPy er ikke nødvendigvis det optimale værktøj til alle de opgaver, vi løser med Python i kurset, men vi har valgt Python fordi det er standardprogrammeringssproget på fysikstudiets førstedel, så de kræfter, du kommer til at bruge på Python, får du forhåbentlig gavn af andre steder (f.eks. i MekRel-kurset). På denne side har vi samlet en række af forskellige noter, som forhåbentlig kan introducerer alt det Sympy, som I kan få brug for i LinAlys kurset.
# 
# Det er vigtigt at være opmærksom på, at modsat CAS-værktøjer som Maple, TI_Nspire og WordMat, så er Python ikke lavet specifikt til symbolske udregninger, men er et generelt anvendeligt programmeringssprog. Man skal derfor vænne sig til både Pythons syntaks og programmering som helhed for at få det maksimale ud af SymPy. Når det til gengæld er klaret, er det muligt at benytte SymPy i en lang række sammenhænge, og f.eks. nemt skifte mellem numeriske og symbolske anvendelser. Dette vil vi vende tilbage til, når vi har forudsætningerne på plads.
# 
