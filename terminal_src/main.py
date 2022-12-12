from smartcard.System import readers
from smartcard.util import toHexString
from utils import *

r=readers()
print(r)
connection = r[0].createConnection()
connection.connect()

#HelloWorld
def hello_robert() -> None:
    print("Calling Hello World...")
    SELECT = [0x80, 0x40, 0x00, 0x00, 0x0B]
    DF_TELECOM =  [0xA0, 0x00, 0x00, 0x00, 0x62, 0x03, 0x01, 0x0C, 0x06, 0x01, 0x02]
    data, sw1, sw2 = connection.transmit( SELECT + DF_TELECOM )
    pretty_printer(data, sw1, sw2)

def get_data() -> None:
    print("Calling Hello World...")
    GETDATA = [0x80, 0x40, 0x00, 0x00, 0x0C]
    data, sw1, sw2 = connection.transmit(GETDATA)
    pretty_printer(data, sw1, sw2)

def change_pin(pincode: list) -> None:
    """Changes the pincode of the javacard
    The pincode needs to be a list of 4 bytes"""
    #TODO verify the length of the pincode
    print("Changing the pin...")
    GETDATA = [0x80, 0x30, 0x00, 0x00, len(pincode)]
    data, sw1, sw2 = connection.transmit(GETDATA + pincode + [0x00])
    pretty_printer(data, sw1, sw2)

def check_pin(pincode: list) -> bool:
    """Changes the pincode of the javacard
    The pincode needs to be a list of 4 bytes"""
    print("Checking the pin...")
    #TODO verify the length of the pincode
    GETDATA = [0x80, 0x01, 0x00, 0x00, len(pincode)]
    data, sw1, sw2 = connection.transmit(GETDATA + pincode)
    pretty_printer(data, sw1, sw2)

get_data()
change_pin(pincode=[0x0, 0x0, 0x0, 0x0])
check_pin(pincode=[0x0, 0x0, 0x0, 0x0])