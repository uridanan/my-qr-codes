import qrcode
from PIL import Image

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




def generate_qr_code_with_logo(data, logo_file, output_file="qr_code.png", fill_color='black', back_color='white', size=10, border=4):
    """Embeds an image in the center of a QR code."""

    try:
        # Create the QR code (adjust version and error correction as needed)
        qr = qrcode.QRCode(
            version=5,  # Start with a lower version; increase if needed
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction is recommended
            box_size=size,
            border=border,
        )
        qr.add_data(data)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGBA")  # Ensure RGB for image pasting

        if logo_file:
            # Load and resize the image
            try:
                logo = Image.open(logo_file).convert("RGBA") # Ensure RGB for image pasting
            except FileNotFoundError:
                print(f"Error: Logo image not found at {logo_file}")
                return

            # Logo size relative to QR width
            qr_width, qr_height = qr_image.size
            max_logo_size = int(qr_width * 0.3)
            logo_w, logo_h = logo.size
            if logo_w > logo_h:
                logo_new_w = max_logo_size
                logo_new_h = round(logo_h * max_logo_size / logo_w)
            else:
                logo_new_h = max_logo_size
                logo_new_w = round(logo_w * max_logo_size / logo_h)

            logo = logo.resize((logo_new_w, logo_new_h), Image.LANCZOS)
            logo_width, logo_height = logo.size
            position = ((qr_width - logo_width) // 2, (qr_width - logo_height) // 2)

            # Create a background image with the QR code's background color
            background = Image.new("RGBA", logo.size, qr_image.getpixel((0, 0)))  # Get top-left pixel color

            # Paste the logo onto the background
            background.paste(logo, (0, 0), logo)

            # Paste the combined logo+background onto the QR code
            qr_image.paste(background, position)


        # Save the combined image
        qr_image.save(output_file)
        print(f"QR code with embedded image saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
