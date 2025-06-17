#!/usr/bin/env python3
"""
Example usage of the pdfpg2img package.
"""

import sys
import logging
from pdfpg2img import PDFPg2Img

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Example usage of PDF2Image converter."""
    
    print("=== High Quality PDF to Image Conversion ===")
    try:
        converter = PDFPg2Img("data/Wolfspeed_C3M0032120K_data_sheet.pdf")
        converter.set_output_path("output_images/")
        converter.set_dpi(600)  # High DPI for best quality
        converter.read_pdf()
        print("✓ High quality conversion completed successfully!")
    except Exception as e:
        print(f"✗ Conversion failed: {e}")


if __name__ == "__main__":
    main() 