import qrcode

def generate_qr_code(link, filename="qr_code.png", fill_color='black', back_color='white'):
    """
    Generates a QR code for a given link and saves it as a PNG image.

    Args:
        link: The URL or text to encode in the QR code.
        filename: The name of the file to save the QR code as (default: qr_code.png).
    """
    try:
        qr = qrcode.QRCode(
            version=1,  # Adjust version for larger data
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Adjust error correction level
            box_size=10,  # Adjust box size for QR code size
            border=4,  # Adjust border size
        )
        qr.add_data(link)
        qr.make(fit=True)  # Make the QR code fit the data

        img = qr.make_image(fill_color=fill_color, back_color=back_color)  # Customize colors
        img.save(filename)
        print(f"QR code saved to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

