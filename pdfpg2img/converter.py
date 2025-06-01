"""
Core PDF to Image conversion functionality.
"""

import os
import logging
import traceback
import numpy as np
import cv2
import fitz  # PyMuPDF

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class PDFPg2Img:
    """
    A class to convert PDF pages to images.
    
    Attributes:
        input_path (str): Path to the input PDF file
        output_path (str): Directory to save the converted images
        dpi (int): DPI (dots per inch) for image resolution
    """
    
    def __init__(self, pdf_file_path=None, output_path="output_images", dpi=300):
        """
        Initialize the PDF2Image converter.
        
        Args:
            pdf_file_path (str, optional): Path to the PDF file to convert
            output_path (str, optional): Output directory for images. Defaults to "output_images"
            dpi (int, optional): DPI for image resolution. Defaults to 300
        """
        self.input_path = pdf_file_path
        self.output_path = output_path
        self.dpi = dpi
    
    def read_pdf(self):
        """
        Process the PDF and save images to output_path.
        
        Raises:
            ValueError: If input path or output path not set
        """
        if not self.input_path or not self.output_path:
            logger.error("Input path or output path not set")
            raise ValueError("Input path or output path not set")
        
        self.process_input(self.input_path, self.output_path)
    
    def process_input(self, pdf_path, result_path):
        """
        Process the PDF file and save images to result_path.
        
        Args:
            pdf_path (str): Path to the PDF file
            result_path (str): Directory to save the images
            
        Raises:
            FileNotFoundError: If PDF file doesn't exist
            RuntimeError: If failed to create result directory
            ValueError: If failed to convert PDF to images
        """
        if not os.path.exists(pdf_path):
            logger.error(f"PDF file does not exist: {pdf_path}")
            raise FileNotFoundError(f"PDF file does not exist: {pdf_path}")
        
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        pdf_result_dir = os.path.join(result_path, pdf_name)
        try:
            os.makedirs(pdf_result_dir, exist_ok=True)
        except Exception as e:
            logger.error(f"Failed to create result directory: {e}\n{traceback.format_exc()}")
            raise RuntimeError(f"Failed to create result directory: {e}")

        try:
            doc = fitz.open(pdf_path)
            page_count = doc.page_count
            logger.info(f"PDF has {page_count} pages")
            
            for page_num in range(page_count):
                page = doc.load_page(page_num)
                pix = page.get_pixmap(matrix=fitz.Matrix(self.dpi/72, self.dpi/72))
                img_data = pix.tobytes("png")
                nparr = np.frombuffer(img_data, np.uint8)
                img_cv = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                
                # Save the image
                img_filename = f"page_{page_num+1}.png"
                img_path = os.path.join(pdf_result_dir, img_filename)
                if cv2.imwrite(img_path, img_cv):
                    logger.info(f"Saved page {page_num+1} to {img_path}")
                else:
                    logger.error(f"Failed to save page {page_num+1}")
            
            doc.close()
            logger.info(f"Successfully processed {page_count} pages")
        except Exception as e:
            logger.error(f"Failed to convert PDF to images: {e}\n{traceback.format_exc()}")
            raise ValueError(f"Failed to convert PDF to images: {e}")

    def set_dpi(self, dpi):
        """
        Set the DPI (dots per inch) for image resolution.
        
        Args:
            dpi (int): DPI value for image resolution
        """
        self.dpi = dpi

    def set_output_path(self, output_path):
        """
        Set the output directory path.
        
        Args:
            output_path (str): Directory path for saving images
        """
        self.output_path = output_path 