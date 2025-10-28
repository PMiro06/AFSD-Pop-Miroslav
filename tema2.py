elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]
# PARTEA A
for i in range(len(elevi)):
    print(f"{elevi[i]} are nota: {note[i]}")
print()
print("A2:")
print()

#Partea B
nota_minima=min(note)
ind_nota_minima=note.index(nota_minima)

nota_maxima=max(note)
ind_nota_maxima=note.index(nota_maxima)

print(f"{elevi[ind_nota_maxima]} are nota maxima: {note[ind_nota_maxima]}")
print(f"{elevi[ind_nota_minima]} are nota minima: {note[ind_nota_minima]}")

print()
print("A3:")
print()
#A3:
s=0
for i in range(len(note)):
    s+=note[i]
med_arit=s/len(note)
print(f"Media aritmetica a clasei este: ", "%.2f"%med_arit)

print()
print("A4:")
print()
#A4:

for i in range(len(note)):
    if note[i]>=5:
        print(f"Elevul {elevi[i]} a trecut clasa cu nota: {note[i]}")

#PARTEA B

for i in range(len(note)):
    if note[i]<10:
        note[i]+=1

print()
print("B6:")
print()
#B6:

note.append(nota_elev_nou)
elevi.append(elev_nou)
print(note, elevi)

print()
print("B7:")
print()
#B7:

ind_elev_de_sters = elevi.index(elev_de_sters)
nota_elev_de_sters = note[ind_elev_de_sters]
note.remove(nota_elev_de_sters)
elevi.remove(elev_de_sters)
print(note, elevi)

print()
print("B8:")
print()

for i in range(len(elevi)):
    print(f"{elevi[i]} are nota: {note[i]}")

#PARTEA C

print()
print("C9:")
print()

ok=0
i=0
while i <= len(interogari_nume):
    if interogari_nume[i]=="stop":
        break
    else:
        if interogari_nume[i] in elevi:
            ind_interogari=elevi.index(interogari_nume[i])
            print(f"Elevul {interogari_nume[i]} are nota {note[ind_interogari]}")
            ok=1
    if ok==0:
        print("nu exista")
    i+=1

print()
print("C10:")
print()
promovati=0
respinsi=0
for i in range(len(note)):
    if note[i]>=5:
        promovati+=1
    else:
        respinsi+=1
print(f"Promovati: {promovati}")
print(f"Respinsi: {respinsi}")

print()
print("C11:")
print()

elevi_promovati=[0]
s=0
for i in range(len(note)):
    if note[i]>=5:
        elevi_promovati.append(note[i])

for i in range(len(elevi_promovati)):
    s=s+elevi_promovati[i]

med_promovati=s/len(elevi_promovati)
if elevi_promovati==0:
    print("nu exista elevi promovati")
else:
    print(f"Media promovati: {"%.2f"%med_promovati}")