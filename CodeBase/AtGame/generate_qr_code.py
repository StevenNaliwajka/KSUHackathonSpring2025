import os
import sys

import qrcode
from qrcode.main import QRCode

from CodeBase.StandardFilePathing.get_project_root import get_project_root


def generate_qr_code(website_url):

    # Create QR code instance
    qr = QRCode(
        version=1,  # Version 1 (21x21 matrix)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
        box_size=10,  # Size of each box in pixels
        border=4,  # Border thickness
    )

    # Add data to the QR code
    qr.add_data(website_url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    qr_image = qr.make_image(fill="black", back_color="white")

    # Save the QR code as an image file
    root = get_project_root()
    qr_image.save(os.path.join(root,"website_qrcode.png"))

    # Show the QR code
    qr_image.show()

if __name__ == '__main__':
    #arguments = sys.argv[1:]
    arguments = "localhost"
    generate_qr_code(arguments[0])