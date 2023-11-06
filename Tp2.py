
# nimewo 1

n = 50  # nomb eleman nan lis la

lis_divizib_pa_de = [i for i in range(n+1) if i % 2 == 0]

print("lis yon bann eleman ki divize pa 2",lis_divizib_pa_de)
print()

#nimewo 2
lis_antye=[0,1,2,3,4,5,6,7,8,9,10,11]

lis_chenn = [str(eleman) for eleman in lis_antye]
print("lis konsyon lis an string :",lis_chenn)
print()

#nimewo 3
lis_chenn_miniskil = ['bonjou', 'bonswa', 'koman ou ye']
lis_chenn_majiskil = [eleman.upper() for eleman in lis_chenn_miniskil]
print("lis yon an majiskil",lis_chenn_majiskil)
print()

#nimewo 4   Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman
lis_apre = [eleman for i, eleman in enumerate(lis_antye) if i % 3 == 0]
print("lis endex ki divize pa 3 ",lis_apre)
print()

#nimero 5  Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tipl
lis_tupl = [tuple(lis_antye[i:i+3]) for i in range(0, len(lis_antye), 3)]
print("lis tiple yo" ,lis_tupl)
print()

# nimewo 6 Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa gen okenn doublon.
    
lis_doublon=[1,3,2,4,3,1,4,5,6,7,8,5,6,7,7,9]
lis_san_doublon = list(set(lis_doublon))
print("lis ak doublon : " ,lis_doublon)
print("lis san doublon :", lis_san_doublon)
print()
#NIMEWO 7  Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo.

lis_eleman_komen = [element for element in lis_antye if  element in lis_apre]
print("lis eleman an komen ant 2 lis:" ,lis_eleman_komen)
print()

#nimewo 8 Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo.
lis_eleman_distenge = [element for element in lis_antye if not  element in lis_apre]
print("lis eleman an pa an  komen ant 2 lis:" ,lis_eleman_distenge)

print()


# nimewo 9  Ou gen yon diksyonè. Kreye yon nouvo lis ak kle yo sèlman, epi yon lòt ak valè yo sèlman.
diksione={'Jb':4, 'dens':22, 'densky':50, 'jbd':'jeanbaptiste'} 
lis_vale= list(diksione.keys())
lis_kle=list(diksione.values())
print("lis ki gen kle yo :",lis_vale)
print("lis ki gen vale yo :",lis_kle)
print()

# nimewo 10 Reyini 3 lis ansanm, san okenn doublon.

lis1 = [1, 2, 3,5, 4, 5]
lis2 = [4, 5, 6,5, 7, 8]
lis3 = [7, 8, 9,10, 10, 11]

lis_reyini = list(set(lis1) | set(lis2) | set(lis3))
print("reyinion 3 lis ansanm san doublou",lis_reyini)




