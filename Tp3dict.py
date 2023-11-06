
import re



# nimewo 1 Ou gen yon diksyonè. Rekipere tout valè yo, gras ak kle yo epi retounen yon lis valè.
mon_diksyone={'Jb':434, 'dens':22 , 'densky':500 , 'jbd':'jeanbaptiste'} 
lis_vale = list(mon_diksyone.values())
print("lis vale yo :",lis_vale)
print()

# nimewo 2 Mande itilizatè a, tape yon valè... epi verifye si l gen akolad devan ak dèyè.


# valè = input("Tape yon valè avèk akolad devan ak dèyè: ")

# while not re.match(r"^\{.*\}$", valè):
#     print("Valè a dwe gen akolad devan ak dèyè.")
#     valè = input("Tape yon valè avèk akolad devan ak dèyè: ")

# print("Valè a korek.")
# print()

#nimero 3 Pakouri yon diksyonè, epi afiche tout kle yo.
print("kle yo :")
for kle  in  mon_diksyone.keys():
    print(kle)


print()

    # nimewo 4 pakoyri yon disyone epi afiche vale yo
print("vale yo :")        
for vale in mon_diksyone.values():
        print(vale)
print()        

        # nimewo 6 Anndan yon diksyonè ki gen kle ak valè(valè yo ka nenpòt tip done).
        #  Ajoute yon  _underscore_  devan ak dèyè tout valè ki se chenn yo

for kle, vale in mon_diksyone.items():
    if isinstance(vale, str):  # Verifye si valè a se yon chenn
      mon_diksyone[kle] = f"_{vale}_"  # Ajoute _ devan ak dèyè valè a
      print("afiche deye vale _ :" , mon_diksyone)
print()

# nimero 7 Nan yon diksyonè ki gen valè ki se chenn sèlman.
#  Kreye yon nouvo diksyonè ki gen tout eleman ki gen valè ki dijit yo sèlman
 

diksyone_chif = {kle: vale for kle, vale in mon_diksyone.items() if isinstance(vale, int)}

print(diksyone_chif)
print()

#NIMERO 8 Pakouri yon disksyonè, pou w mete l sou fòm lis, 
# kote chak eleman nan disksyonè sa, vin sou fòm tipl(kle, valè) anndan lis la

lis_tipl = list(mon_diksyone.items())
print(lis_tipl)
print()

# NIMEWO 9 Pakouri yon lis tipl, pou w mete l sou fòm diksyonè

mon_diksyone = dict(lis_tipl)
 # NIMERO 10 

 # Egzanp dwe kreye 2 diksyonè:
diksyone1 = {'JB': 123, 'JBD': 'bonjou', 'lis': [1, 2, 3], 'jn': 'jb'}
diksyone2 = {'tit': '678', 'dict': {1, 2, 3}, 'python': 456, 'py': '54'}


def kole_diksyone(diksyone1, diksyone2):
    nouvo_diksyone = {}

    for kle, vale in diksyone1.items():
        tip_vale = type(vale)

        if tip_vale == int:
            nouvo_diksyone[kle] = "ADISYON"
        elif tip_vale in [str, list, set]:
            nouvo_diksyone[kle] = "KONKATENASYON"

    for kle, vale in diksyone2.items():
        tip_vale = type(vale)

        if tip_vale == int:
            nouvo_diksyone[kle] = "ADISYON"
        elif tip_vale in [str, list, set]:
            nouvo_diksyone[kle] = "KONKATENASYON"

    return nouvo_diksyone


# Kole yo ansanm
rezilta = kole_diksyone(diksyone1, diksyone2)

print(rezilta)






