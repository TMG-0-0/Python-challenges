# Create a QR code that stores URLs.

import qrcode
img = qrcode.make("https://www.youtube.com/")
type(img)
img.save("Youtube.png")