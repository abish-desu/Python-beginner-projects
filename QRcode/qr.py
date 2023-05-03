# Simple method to print qr code
import qrcode as qr
image =  qr.make("https://www.facebook.com/profile.php?id=100072383365916")
image.save("Riya profile.png")

