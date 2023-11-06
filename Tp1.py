
#mete yon chen karacte an miniskil
mo="WAW HELLO Guys Wellcome Back a"

m=mo.lower()
print(m )
print()

# nimewo 2
nom="Ayibobo ayiti"
rep=nom.split()
print(rep)
print()

#nimero 3bb
rep2=nom.title()
print(rep2)
print()

# nimewo 4   
nouvo_mo = [let[0] for let in mo.split()]
init="".join(nouvo_mo)
print(init)


#nimewo 5
rep4=rep2.replace("A" ,"@")
print(rep4)
print()

#nimewo 6
rep5="".join(reversed(nom))
rep6=rep5.upper()

print(rep6)
print()


# nimewo 7
index=mo.index("a")
print(index)
print()

# nimero 8 e 9
chenn = "Ayiti kapab avanse"
index_a = []
for i, let in enumerate(chenn):
    if let.lower() == "a":
        index_a.append(i)

som_index_a = sum(index_a)

print("Les indexes de 'a' sont:", index_a)
print("La somme des indexes de 'a' est:", som_index_a)
print()

# nimewo 10

chenn_san_espas = chenn.replace(" ", "")
kantite_karakte_sans_espas = len(chenn_san_espas)

print("Chenn san espas:", chenn_san_espas)
print("Kantite karaktè san espas:", kantite_karakte_sans_espas)
