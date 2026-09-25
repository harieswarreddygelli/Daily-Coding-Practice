import qrcode 
from PIL import Image
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=5,
    border=2   
)
qr.add_data("github.com/harieswarreddygelli")
qr.make(fit=True)
git=qr.make_image(fill_color="Black",back_color="Orange").convert("RGB")
try:
    logo=Image.open("logo.png")
    qr_width, qr_height = git.size
    logo=logo.resize((80,80),Image.Resampling.LANCZOS)
    position = ((qr_width - 80) // 2, (qr_height - 80) // 2)
    git.paste(logo, position)
except FileNotFoundError:
    print(
        "Logo file not found! Generating QR code without a logo (make sure 'logo.png' exists)."
    )
git.save("Githuwithlogo.png")
print("="*10,"Sucessful","="*10)
