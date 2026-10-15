import qrcode
url=input("Enter Your URL").strip()
file_path="D:\\Python27\\qrcode.png"
qr=qrcode.QRCode()
qr.add_data(url)
img=qr.make_image()
img.save(file_path)
print("This is u r qrcode")