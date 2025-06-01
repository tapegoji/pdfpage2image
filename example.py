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
    
    # Example 1: Basic usage
    print("=== Example 1: Basic Usage ===")
    try:
        converter = PDFPg2Img("data/Wolfspeed_C3M0016120K_data_sheet.pdf")
        converter.read_pdf()
        print("✓ Basic conversion completed successfully!")
    except Exception as e:
        print(f"✗ Basic conversion failed: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Example 2: Custom settings
    print("=== Example 2: Custom Settings ===")
    try:
        converter = PDFPg2Img(
            pdf_file_path="data/Wolfspeed_C3M0016120K_data_sheet.pdf",
            output_path="output_images/custom_output",
            dpi=150
        )
        converter.read_pdf()
        print("✓ Custom settings conversion completed successfully!")
    except Exception as e:
        print(f"✗ Custom settings conversion failed: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Example 3: Dynamic configuration
    print("=== Example 3: Dynamic Configuration ===")
    try:
        converter = PDFPg2Img("data/Wolfspeed_C3M0016120K_data_sheet.pdf")
        converter.set_output_path("output_images/dynamic_output")
        converter.set_dpi(600)
        converter.read_pdf()
        print("✓ Dynamic configuration conversion completed successfully!")
    except Exception as e:
        print(f"✗ Dynamic configuration conversion failed: {e}")


if __name__ == "__main__":
    main() 