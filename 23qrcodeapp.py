#qrcode generation from your name
import qrcode
# name=input("Enter your name:")
# img=qrcode.make(name)
# type(img)
# img.save(f"{name}.png")

name="https://technologychannel.org/"
img=qrcode.make(name)
type(img)
img.save("{name}.png")