
import qrcode

def generate_qr(data,filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 10,
        border = 4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill = 'black', back_color = 'white')
    img.save(filename)
    print(f'qr code saved as {filename}')

data = "https://www.w3schools.com"
filename = "qrcode.png"
generate_qr(data,filename)


