import qrcode
import sys
# Create an image from the QR code instance
def QR(a,b):
    qr = qrcode.make(a)
# Save the image
    qr.save(b)
if __name__ == "__main__":
    # First is link, second is name of QR pic
    name = str(sys.argv[2]) + ".png"
    QR(sys.argv[1],name)