"""
Pol Sánchez, Dídac Lloret, Rubén Sánchez
ASIXc1B
Programa de càlcul de temperatures del mar.
Calcula per a l’any  2022: temperatura màxima, mínima i mitjana
Calcula per període 2000 a 2022: temperatura màxima, mínima i mitjana

"""
datos_climaticos = {
    2000: (12.7, 12.4, 12.6, 12.4, 13, 13.6, 13.3, 13.6, 13.5, 15.9, 15.3, 14.9),
    2001: (13.8, 13, 12.6, 13.6, 13.5, 13.4, 14, 14, 14.2, 15.3, 16.8, 14),
    2002: (13.2, 12.4, 12.9, 13.4, 13.7, 13.6, 14.4, 13.8, 14.3, 14.8, 15.3, 14.2),
    2003: (13.6, 12.2, 12.5, 12.8, 14.7, 13.5, 13.6, 13.7, 14.2, 15.9, 15.3, 15),
    2004: (13.5, 12.7, 12.3, 12.6, 13.2, 13.1, 13.3, 13.6, 14.9, 15.3, 15.4, 14.6),
    2005: (13.3, 12.3, 12.3, 12.9, 13.4, 13.3, 13.3, 13.4, 13.9, 15.2, 17.1, 14.4),
    2006: (12.5, 12.3, 12.1, 12.9, 13.1, 13.4, 13.2, 13.2, 14, 15.5, 17.3, 15.8),
    2007: (14.3, 13.4, 13.2, 13.4, 14.4, 13.8, 13.8, 13.8, 14, 15.5, 15.5, 13.9),
    2008: (13.2, 13, 12.9, 12.8, 13.3, 13.6, 13.7, 13.8, 13.9, 14.3, 15.5, 13.8),
    2009: (13.3, 12.5, 12.6, 12.8, 14.2, 13.7, 13.7, 13.8, 14, 16.2, 15.9, 14.5),
    2010: (12.6, 11.9, 12.2, 12.8, 13.7, 13.6, 13.5, 13.5, 13.9, 15.6, 15.5, 14),
    2011: (13, 12.5, 12.5, 13.6, 13.5, 14, 14.1, 13.7, 13.8, 15.2, 17.6, 15.9),
    2012: (13.9, 12.4, 12.6, 13.3, 13.7, 13.5, 13.5, 13.7, 13.9, 14.8, 15.8, 13.9),
    2013: (13.2, 12.2, 12, 13.1, 13.5, 14.1, 13.7, 13.6, 13.6, 15.3, 15.9, 13.6),
    2014: (13.7, 13.2, 13.6, 13.6, 14.7, 14.2, 13.9, 14, 14.5, 15.7, 16.5, 16),
    2015: (14.1, 12.6, 12.9, 13.5, 14.3, 13.9, 13.7, 13.8, 14.1, 15.8, 15.8, 15.1),
    2016: (14.1, 13.6, 12.9, 13.5, 14, 13.9, 14, 14, 14.2, 16.3, 16.5, 15.6),
    2017: (13.7, 12.8, 13.4, 13.9, 14, 14, 13.9, 14, 14, 14.6, 14.8, 13.3),
    2018: (13.2, 12.7, 12.3, 12.9, 13.8, 13.9, 14, 14.1, 14.3, 17.9, 17.7, 15.9),
    2019: (13.9, 12.5, 13.3, 13.4, 14, 13.9, 13.8, 13.9, 14.5, 14.9, 15.5, 15.4),
    2020: (14.4, 13.9, 13.6, 13.5, 13.7, 13.9, 13.9, 14, 14.3, 14.7, 15.6, 14.6),
    2021: (13.3, 12.9, 13.5, 13.5, 13.7, 13.8, 13.8, 13.8, 14.2, 14.6, 16.8, 14.7),
    2022: (13.6, 13.4, 13.2, 13.4, 13.9, 13.7, 13.7, 13.8, 14, 14.3, 16, 15.1)
}

temperaturamax2022 = 0
temperaturamin2022 = 100
temperaturamitjana2022 = 0

temperaturamax= 0
temperaturamin= 100
temperaturamitjana= 0
mitjana2 = 0

for temperatura2022 in datos_climaticos[2022]:
    if temperatura2022 > temperaturamax2022:
        temperaturamax2022 = temperatura2022
    if temperatura2022 < temperaturamin2022:
        temperaturamin2022 = temperatura2022
    temperaturamitjana2022 += temperatura2022

mitjana2022 = round(temperaturamitjana2022/len(datos_climaticos[2022]), 2)

contador = 0
for key in datos_climaticos.keys():
    for temperatura in datos_climaticos[key]:
        if temperaturamax < temperatura:
            temperaturamax = temperatura
        if temperaturamin > temperatura:
            temperaturamin = temperatura
        temperaturamitjana += temperatura
        contador += 1

mitjana = round(temperaturamitjana/contador,2)
print(temperaturamax2022, temperaturamin2022, mitjana2022)
print(temperaturamax, temperaturamin, mitjana)