"""
Rubén Sánchez Campaner
1.B
PARAULES
"""
count=0
c = 1
p = []
ma = []
c = 1
try:
    while True:
        pa = input()
        count=count+1
        if pa == '\q' or count == 1000000:
            break
        p.append(pa)
    for i in p:
        lo = len(i)
        ma.append(lo)
except:
    print("ERROR")

print(f"Lista de palabras: {p} \n")
print(f"La más larga: {max(ma)}")
print(f"La más corta: {min(ma)}")
print(f"Media de caracteres de todas las palabras introducidas: {sum(ma)/len(ma)}")
tu = tuple(p)

for i in tu:
    lon = len(i)
    print(f"Palabra {c}: {i} | Mide: {lon} ")
    c = c + 1
