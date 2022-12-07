from smartcard.System import readers
from smartcard.util import toHexString

r=readers()
print(r)
connection = r[0].createConnection()
connection.connect()

#HelloWorld
def hello_robert() -> None:
    SELECT = [0x80, 0x40, 0x04, 0x00, 0x0B]
    DF_TELECOM =  [0xA0, 0x00, 0x00, 0x00, 0x62, 0x03, 0x01, 0x0C, 0x06, 0x01, 0x02]
    data, sw1, sw2 = connection.transmit( SELECT + DF_TELECOM )
    print(f"data : {data}")

def get_data() -> None:
    GETDATA = [0x80, 0x40, 0x00, 0x00, 0x0C]
    data, sw1, sw2 = connection.transmit(GETDATA)
    print("%x %x" % (sw1, sw2))
    print('data:', data)

def change_pin(pincode: list) -> None:
    """Changes the pincode of the javacard
    The pincode needs to be a list of 4 bytes"""
    #TODO verify the length of the pincode
    GETDATA = [0x80, 0x30, 0x00, 0x00, len(pincode)]
    data, sw1, sw2 = connection.transmit(GETDATA + pincode)
    print(f"return code : {sw1} {sw2}")

change_pin([0x0, 0x0, 0x0, 0x0])