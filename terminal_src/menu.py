from utils import * 
from smartcard.System import readers
from smartcard.util import toHexString
from utils import *

r=readers()
connection = r[0].createConnection()
connection.connect()

def check_connection() -> None:
    """Sends the hello world APDU to the javacard"""
    print("Vérification de la connection...")
    GETDATA = [0x80, 0x40, 0x00, 0x00, 0x0C]
    data, sw1, sw2 = connection.transmit(GETDATA)
    pretty_printer(data, sw1, sw2)

def change_pin(pincode: list) -> None:
    """Changes the pincode of the javacard
    The pincode needs to be a list of 4 bytes"""
    print("Changement du pin...")
    GETDATA = [0x80, 0x30, 0x00, 0x00, len(pincode)]
    data, sw1, sw2 = connection.transmit(GETDATA + pincode + [0x00])
    pretty_printer(data, sw1, sw2)

def check_pin(pincode: list) -> bool:
    """Changes the pincode of the javacard
    The pincode needs to be a list of 4 bytes"""
    print("Vérification du pin...")
    GETDATA = [0x80, 0x01, 0x00, 0x00, len(pincode)]
    data, sw1, sw2 = connection.transmit(GETDATA + pincode)
    pretty_printer(data, sw1, sw2)

def main_menu():
    print("Bienvenue dans l'interface de gestion de la javacard")
    while True:
        menu_printer()
        fonct = input()
        try:
            value = int(fonct)
        except Exception as e:
            print("Valeur inconnue, veuillez réessayer\n")
            continue

        try:
            #Connectivity (hello world)
            if value == 1:
                check_connection()
                continue

            #Setting the pincode
            if value == 2:
                val = clean_pincode(pincode_printer())
                if val != 1:
                    change_pin(val)
                continue
            
            #Checking the pincode
            if value == 3:
                val = clean_pincode(pincode_printer())
                if val != 1:
                    check_pin(val)
                continue

            #Quit
            if value == 4:
                print("Fin du programme !")
                return
        except Exception as e:
            print(e)
            print("Erreur, retour au menu")
            continue
            
        
        


