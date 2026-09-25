import qrcode 
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=5,
    border=2   
)
qr.add_data("github.com/harieswarreddygelli")
qr.make(fit=True)
git=qr.make_image(fill_color="Orange",back_color="White")
git.save("Custom.png")
