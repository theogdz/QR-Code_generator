import qrcode
import sys

# Create an image from the QR code instance
def QR(link,name):
    qr = qrcode.make(link)
# Save the image
    qr.save(name)

if __name__ == "__main__":
    # First is link, second is name of QR pic
    link = input("Enter the link:\n")
    name = "img\\" + input("How should we name the QR code? \n") + ".png"
    QR(link,name)