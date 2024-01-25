"""
Pol Sánchez, Dídac Lloret, Rubén Sánchez
ASIXc1B
Programa de traducció d’insults. Crear una estructura de dues dimensions amb els insults en català i afegir la traducció en castellà, anglès i nepalí
"""
CAT = 0
ESP = 1
ENG = 2
NEP = 3

insults = [
    ["Malparit", "Bufetes", "Brètol", "Llanut", "Borinot", "Banyut", "Bagassa", "Beneit", "Llepaculs", "Nyèbit"],
    ["Malparido", "Bufetes", "Brutote", "Llano", "Tonto, simple", "Cuernudo", "Prostituta", "Bendito", "Lameculos", "Niñato"],
    ["Bastard", "Lawyers", "Brute", "Flat, Plain", "Silly", "Horned", "Prostitute", "Blessed", "Ass-licker", "Brat"],
    ["बास्टर्ड", "वकील", "ब्रुट", "फ्लैट, प्लेन", "सिली", "सिङ्ग", "वेश्या", "धन्य", "गधा चाट्ने", "ब्याट"]
]


while True:
    insult = input('Introdueix un insult en català (o "exit" per sortir): ')


    try:
        index = insults[CAT].index(insult)
        traduccio_cat, traduccio_esp, traduccio_eng, traduccio_nep = insults[CAT][index], insults[ESP][index], insults[ENG][index], insults[NEP][index]

        print(f'Insult en català: {traduccio_cat}')
        print(f'Traducció a castellà: {traduccio_esp}')
        print(f'Traducció a anglès: {traduccio_eng}')
        print(f'Traducció a nepalí: {traduccio_nep}')

    except ValueError:
        print('Insult no trobat en la llista. Torna-ho a provar.')


