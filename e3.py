"""
Pol Sánchez, Dídac Lloret, Rubén Sánchez
ASIXc1B
Programa de traducció d’insults. Crear una estructura de dues dimensions amb els insults en català i afegir la traducció en castellà, anglès i klingon
"""

ins = input("Introdueix un insult en català: ")
try:

    CAT = 0
    ESP = 1
    ENG = 2
    NEP = 3

    insults = [
        ["Malparit" "Bufetes" "Brètol" "Llanut" "Borinot" "Banyut" "Bagassa" "Beneit" "Llepaculs" "Nyèbit"],
        ["Malparido" "Bufetes" "Brutote" "Llano" "Tonto, simple" "Cuernudo" "Prostituta" "Bendito" "Lameculos" "Niñato"],
        ["Bastard" "Lawyers" "Brute" "Flat, Plain" "Silly" "Horned" "Prostitute" "Blessed" "Ass-licker" "Brat"],
        ["बास्टर्ड" "वकील" "ब्रुट" "फ्लैट, प्लेन" "सिली" "सिङ्ग" "वेश्या" "धन्य" "गधा चाट्ने" "ब्याट"]
    ]

    # Bucle per demanar insults a l'usuari





    if ins in insults[CAT]:
        index_insult_cat = insults[CAT].index(ins)

        print(f"En català: {ins}")
        print(f"En castellà: {insults[ESP][index_insult_cat]}")
        print(f"En anglès: {insults[ENG][index_insult_cat]}")
        print(f"En klingon: {insults[NEP][index_insult_cat]}")
    else:
        print("Insult no trobat. Prova'n un altre.")
except ValueError:
    print("No correct")



