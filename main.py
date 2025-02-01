import qrcode

img = qrcode.make('Rustam')

type(img)

print("rasm yaratildi")
img.save("rasm.png")