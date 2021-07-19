#!/usr/bin/env python
# coding: utf-8

# __Foreslået ændringer__  
# Dette er mere af en intro nu

# # Python i LinAlys
# 
# LinALys-kurset indeholder to spor (analyse og lineær algebra) og har fokus på "blyantsregning" og forståelse af den bagvedliggende teori. Ind imellem får vi brug for et værktøj til at tegne funktioner og foretage både numeriske og symbolske beregninger for at illustrere en problemstilling og/eller støtte eller kontrollere beregningerne i hånden. I år har vi valgt at bruge Python-modulet SymPy som CAS-værktøj (Computer Algebra System). Python og SymPy er ikke nødvendigvis det optimale værktøj til alle de opgaver, vi løser med Python i kurset, men vi har valgt Python fordi det er standardprogrammeringssproget på fysikstudiets førstedel, så de kræfter, du kommer til at bruge på Python, får du forhåbentlig gavn af andre steder (f.eks. i MekRel-kurset). Dette dokument er det første af en række notebooks, der introducerer de nødvendige koncepter.
# 
# Det er vigtigt at være opmærksom på, at modsat CAS-værktøjer som Maple, TI_Nspire og WordMat, så er Python ikke lavet specifikt til symbolske udregninger, men er et generelt anvendeligt programmeringssprog. Man skal derfor vænne sig til både Pythons syntaks og programmering som helhed for at få det maksimale ud af SymPy. Når det til gengæld er klaret, er det muligt at benytte SymPy i en lang række sammenhænge, og f.eks. nemt skifte mellem numeriske og symbolske anvendelser. Dette vil vi vende tilbage til, når vi har forudsætningerne på plads.
# 
