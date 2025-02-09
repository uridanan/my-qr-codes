# QR Code Generator Package

This Python package provides a simple and reusable way to generate QR codes, 
optionally embedding a logo and customizing colors and sizes.
The package offers 2 methods
**generate_qr_code_bytes:** returns the image data for use in rendering
**generate_qr_code_file:** saves the image to a file and returns the path

## Installation

```bash
pip install qr_generator
```

## Usage
    from qr_generator import generate_qr_code_bytes, generate_qr_code_file

### Basic usage (URL is required)
    image_bytes = generate_qr_code_bytes(data="[https://www.example.com](https://www.example.com)")
    image_path = generate_qr_code_file(data="[https://www.example.com](https://www.example.com)", 
                                           output_file="my_qr_code.png")

### With a logo and custom colors/sizes
    image_path = generate_qr_code_file(
        data="[https://www.example.com](https://www.example.com)",
        output_file="my_qr_code.png"
        logo_file="path/to/your/logo.png",  # Path to your logo image (PNG, JPG)
        back_color="blue",  # Background color (e.g., "white", "#FFFFFF", "rgb(255, 255, 255)")
        fill_color="yellow",  # Fill color (e.g., "black", "#000000", "rgb(0, 0, 0)")
        size=20,  # Size of the QR code (adjust as needed)
        border=2 # Size of the border (adjust as needed)
    )

## Web-app example
    from flask import Flask, send_from_directory
    from qr_generator import generate_qr_code_with_logo
    
    app = Flask(__name__)
    
    @app.route("/qr")
    def generate_qr():
        qr_code_path = "my_qr_code.png"
        generate_qr_code_file(
            data="[https://www.example.com](https://www.example.com)",
            output_file=qr_code_path
            logo_file="path/to/your/logo.png",  # Path to your logo image (PNG, JPG)
            back_color="blue",  # Background color (e.g., "white", "#FFFFFF", "rgb(255, 255, 255)")
            fill_color="yellow",  # Fill color (e.g., "black", "#000000", "rgb(0, 0, 0)")
            size=20,  # Size of the QR code (adjust as needed)
            border=2 # Size of the border (adjust as needed)
        )    
        if qr_code_path:  # TODO: fix this to test for the existence of the file
            return send_from_directory(directory='.', filename=qr_code_path) # Or a full path
        else:
            return "Error generating QR code", 500
    
    if __name__ == "__main__":
        app.run(debug=True)


## Parameters
The generate_qr_code_file function accepts the following parameters:

* data (required): The data to encode in the QR code (usually a URL or text).
* output_file (optional): the filename under which to save the QR code once generated. 
  If not provided, the QR code will be saved as "qr_code.png"
* logo_file (optional): Path to your logo image (PNG, JPG)
* back_color (optional): Background color of the QR code (default: "white"). Can be a color name (e.g., "white", "black", "red"), a hex code (e.g., "#FFFFFF", "#000000"), or an RGB value (e.g., "rgb(255, 255, 255)").
* fill_color (optional): Fill color of the QR code modules (default: "black"). Uses the same color format as bg_color.
* size (optional): Size of the QR code (default: 10). This value influences the box_size used by the qrcode library. A larger value makes a larger QR code.
* border (optional): Size of the border around the QR code (default: 4). This value influences the border parameter used by the qrcode library. The border size cannot exceed 10% of the qr_size.


## Dependencies
* qrcode
* Pillow (PIL fork)