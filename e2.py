"""
Pol Sànchez, Dídac Lloret, Rubén Sànchez
ASIXc 1B
25/01/2024
Programa que generi una llista de 100 nombres aleatoris entre 1 i 50.
Obtenir la mitja dels nombres que es troben a les posicions parelles i la mitja del nombre de les posicions senars.
"""
import random
llista_aleatoria = [random.randint(1, 50) for i in range(100)]
sumparells = 0
sumsenars = 0
print("Amb els nombres:", end=' ')
#bucle que recolecta els parells i els suma
for i in range(0, 99, 2):
    sumparells = (llista_aleatoria[i]) + sumparells
#bucle que recolecta els senars i esl suma
for j in range(1, 99, 2):
    sumsenars = (llista_aleatoria[j]) + sumsenars
#bucle que printa la llista de numeros aleatoris
for elemento in llista_aleatoria:
    print(elemento, end=',')
#calcul de les mitjanes
mitjana_parells = sumparells / 50
mitjana_senars = sumsenars / 50
print()
print(f'Mitjana posicions parelles:', mitjana_parells)
print(f'Mitjana posicions senars:', mitjana_senars)





