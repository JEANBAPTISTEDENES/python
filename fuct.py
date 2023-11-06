import random
import string
import re

# nimewo 1
# kreye yon fonksyon ki ap pran yon paramèt yon mo, epi li retounen envès la.
def fonksyon_inves (mo):
    inves=mo[::-1]
    return inves
inves = fonksyon_inves("python langaj intepretasyon")
print("fonction inves :",inves)
print("*********************************************************")



# nimewo 2 kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik
def fonct_jenere(n):
    karakte = string.ascii_letters  # Kombinasyon nan lèt minis ak majis
    kod = ''.join(random.choice(karakte) for _ in range(n))
    return kod
kod_aleatwa=fonct_jenere(6)
print("kod aleatwa :",kod_aleatwa)
print("*******************************************************************************************")

# 3 kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik, san repetisyon
def kod_jenere_san_rep(n):
    karakte = list(string.ascii_letters)  # Kreye yon list lèt nan alfabè
    kod = ''.join(random.sample(karakte, n))
    return kod
kod_aleatwa=kod_jenere_san_rep(6)
print("kod aleatwa san repetiyson :",kod_aleatwa)
print("************************************************************************************************")

# nimero 4 
# kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alafanimerik, san repetisyon.
def kod_jenere_san_rep(n):
    karakte = list(string.ascii_letters + string.digits)  # Kreye yon list lèt nan alfabè
    kod = ''.join(random.sample(karakte, n))
    return kod
kod_aleatwa=kod_jenere_san_rep(6)
print("kod aleatwa san repetiyson avk alfanimerik:",kod_aleatwa) 
print("****8*******************************************************************************************")

# nimero 5 

def fonct_SLUP(chenn):
    
    
    chenn_san_karaktè_entezi = re.sub(r'[^\w-]', '', chenn)  # Retire tout karaktè ki pa se lèt, chif, oswa "-"
    slug = chenn_san_karaktè_entezi.lower().replace(" ", "-")  # Konvèti nan lòt chenn ak "-" 
    return slug

chenn_orijinal = "Sa se yon chenn! Nimerik 123 ak Espas." 
slug =fonct_SLUP (chenn_orijinal)
print(slug) 
print("************************************************* ****************************************")

# Kreye yon fonksyon ki ap separe chak lèt nan yon mo ak yon vigil
def fonct_delimite(mo, delimite):
    
    mo_separe = delimite.join(list(mo))
    return mo_separe

mo = "Python"
vijil = ","
mo_separe = fonct_delimite(mo, vijil)
print(mo_separe)  
print("************************************************* ****************************************")

# nimewo 7tb
"""
    Fonksyon sa kripte yon mo avèk endèks li nan alfabè a. Chak karaktè dwe separe ak yon tirè.
    """ 

def kripte_alfabetik(mot):
    
    mo_kripte = '-'.join(str(ord(c.lower()) - ord('a')) for c in mot if c.isalpha())
    return mo_kripte


kòd_kripte = kripte_alfabetik("PYTHON")
print(f"Afiche kòd kripte a ",kòd_kripte)   
#nimewo 8
def dekripte_alfabetik(kod):
    """
    Fonksyon sa dekripte yon mo ki fèt ak endèks chak lèt nan alfabè a, separe ak yon tirè.
    """
    endeks = kod.split('-')
    mo_dekripte = ''.join(chr(int(endek) + ord('a')) for endek in endeks)
    return mo_dekripte

kod_kripte = "0-11-14-1-1"
mo_dekripte = dekripte_alfabetik(kod_kripte)
print(" Afiche mo a dekripte",mo_dekripte)  
print("************************************************* ****************************************")

#nimewo 9
def retounen_vale(val1, val2):
    """
    Fonksyon sa pran 2 paramèt epi retounen yo sou fòm Tuple.
    """
    return (val1, val2)

vale1 = 10
vale2 = "python"
rezilta = retounen_vale(vale2, vale1)
print(" Afiche rezilta yo sou fòm Tuple :",rezilta) 
print("************************************************* ****************************************")

# nimewo 10
def inisyal_non(non):
    """
    Fonksyon sa pran yon non kòm paramèt, epi li retounen inisyal yo.
    """
    inisyal = ""
    mo = non.split('-')
    mo_konpoze=non.split(" ")

      # Divize non yo si gen tirè
    for mo in mo_konpoze and mo:
    
        inisyal += mo[0].upper()  # Ajoute premye lèt nan mo yo nan inisyal yo
    return inisyal

# Eksperyans d'itilizasyon :
non = "Jean-Baptiste Jean"

inisyal = inisyal_non(non)
print(inisyal)  # Afiche inisyal yo

''

