import time
def pretty_printer(data, sw1, sw2):
    print("return code : %x %x" % (sw1, sw2))
    print(f"returned data : {data}")
    print("-="*20+"-")

def menu_printer():
    time.sleep(.75)
    print("\nVeuillez séléctionner une fonctionnalité(1/2/3) :")
    print("\t1) Vérifier la connection avec la carte")
    print("\t2) Changer le code PIN")
    print("\t3) Vérifier le code PIN")
    print("\t4) Quitter")

def clean_pincode(pincode):
    try:
        pincode = pincode.replace(" ","").strip()
        pincode = [int(d) for d in pincode]
        if len(pincode) == 4:
            return pincode
        print("Mauvaise taille de pincode, veuillez réessayer")
        return 1
    except Exception as e:
        print(e)
        print("Impossible de parser le pincode, veuillez réessayer")
        return 1


def pincode_printer():
    print("Les codes pins sont 4 valeurs numériques comprises entre 0 et 9")
    print("Pour envoyer un code pin veuillez suivre le format suivant :")
    print("n1n2n3n4 (ou chacun des n correspond à un des nombres)")
    print("Exemple: Le code 1 2 3 4 devra être entré ainsi : 1234")
    return input("Veuillez insérer un code pin :")