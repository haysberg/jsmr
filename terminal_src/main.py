from smartcard.System import readers
from smartcard.util import toHexString

r=readers()
print(r)
connection = r[0].createConnection()
connection.connect()
SELECT = [0x00, 0xA4, 0x04, 0x00, 0x0B]
DF_TELECOM =  [0xA0, 0x00, 0x00, 0x00, 0x62, 0x03, 0x01, 0x0C, 0x06, 0x01, 0x02]

data, sw1, sw2 = connection.transmit( SELECT + DF_TELECOM )
print(data)
print ("%x %x" % (sw1, sw2))

# apdu to getdata
GETDATA = [0x80, 0x40, 0x00, 0x00, 0x0C]
data, sw1, sw2 = connection.transmit(GETDATA)
print("%x %x" % (sw1, sw2))
print('data:', data)