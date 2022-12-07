package src.main.java.main;

/**
 * 
 */
import javacard.framework.Applet;
import javacard.framework.ISO7816;
import javacard.framework.ISOException;
import javacard.framework.OwnerPIN;
import javacard.framework.APDU;
import javacard.framework.Util;

/**
 * @author Robert
 *
 */
public class Main extends Applet {

    private final static byte[] hello = { 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x72, 0x6f, 0x62, 0x65, 0x72, 0x74 };
    OwnerPIN pin = new OwnerPIN((byte) 20, (byte) 4);
    public byte[] pincode = new byte[4]; 
    
    public static void install(byte[] buffer, short offset, byte length)

    {
        // GP-cOFFSET_CDATAompliant JavaCard applet registration
        new Main().register();
    }

    public void process(APDU apdu) {
        // Good practice: Return 9000 on SELECT
        if (selectingApplet()) {
            return;
        }

        byte[] buf = apdu.getBuffer();
        switch (buf[ISO7816.OFFSET_INS]) {
            case (byte) 0x40:
                Util.arrayCopy(hello, (byte) 0, buf, ISO7816.OFFSET_CDATA, (byte) 12);
                apdu.setOutgoingAndSend(ISO7816.OFFSET_CDATA, (byte) 12);
                break;

            // case to add the pincode to the card
            case (byte) 0x30:
                Util.arrayCopy(buf, ISO7816.OFFSET_CDATA, pincode, (short)0, (byte) 4);
                pin.update(buf, ISO7816.OFFSET_CDATA, (byte) 4);
                return;

            case (byte) 0x20:
                if (pin.isValidated()) {
                    Util.arrayCopy(hello, (byte) 0, buf, ISO7816.OFFSET_CDATA, (byte) 12);
                    apdu.setOutgoingAndSend(ISO7816.OFFSET_CDATA, (byte) 12);
                } else {
                    ISOException.throwIt(ISO7816.SW_SECURITY_STATUS_NOT_SATISFIED);
                }
                return;

            case (byte) 0x50:
            //TODO remove the pincode var after the tests are working
                Util.arrayCopy(pincode, (byte) 0, buf, ISO7816.OFFSET_CDATA, (byte) 4);
                apdu.setOutgoingAndSend(ISO7816.OFFSET_CDATA, (byte) 4);
                break;

            default:
                // good practice: If you don't know the INStruction, say so:
                ISOException.throwIt(ISO7816.SW_INS_NOT_SUPPORTED);
        }
    }
}