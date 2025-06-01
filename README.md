# PDF Page to Image Converter

A simple Python package to convert PDF pages to images. This tool extracts each page from a PDF file and saves it as a separate PNG image.

## Features

- Convert each page of a PDF to a high-quality PNG image
- Configurable resolution (DPI)
- Organized output with each PDF's images in its own folder
- Detailed logging
- Easy to import and use programmatically
- Proper Python package structure

## Requirements

- Python 3.6+
- Required packages:
  - numpy
  - opencv-python (cv2)
  - PyMuPDF (fitz)

## Installation

### From Source

1. Clone this repository:
   ```bash
   git clone https://github.com/tapegoji/pdfpage2image.git
   cd pdfpage2image
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install in development mode:
   ```bash
   pip install -e .
   ```

### From PyPI (when published)

```bash
pip install pdfpage2image
```

## Usage

### Basic Usage

```python
from pdfpg2img import PDF2Image

# Simple usage with default settings
converter = PDF2Image("path/to/your/file.pdf")
converter.read_pdf()
```

### Advanced Usage

```python
from pdfpg2img import PDF2Image

# Custom output directory and DPI
converter = PDF2Image(
    pdf_file_path="path/to/your/file.pdf",
    output_path="my_images",
    dpi=600
)
converter.read_pdf()
```

### Alternative Configuration

```python
from pdfpg2img import PDF2Image

# Configure after instantiation
converter = PDF2Image("path/to/your/file.pdf")
converter.set_output_path("custom_output")
converter.set_dpi(150)
converter.read_pdf()
```

## Examples

### Running the Example Script

```bash
python example.py
```

### Running the Main Script

```bash
python pdfpg2img.py
```

## API Reference

### Constructor Parameters

- `pdf_file_path` (str): Path to the PDF file to convert
- `output_path` (str, optional): Output directory for images (default: "output_images")
- `dpi` (int, optional): DPI for image resolution (default: 300)

### Methods

- `read_pdf()`: Convert the PDF to images
- `set_dpi(dpi)`: Change the DPI setting
- `set_output_path(path)`: Change the output directory

## Development

### Building the Package

```bash
python -m build
```

### Installing in Development Mode

```bash
pip install -e .
```

## Package Structure

```
pdfpage2image/
├── pdfpg2img/
│   ├── __init__.py
│   └── converter.py
├── data/
├── example.py
├── pdfpg2img.py
├── setup.py
├── pyproject.toml
├── MANIFEST.in
├── LICENSE
└── README.md
```

## How It Works

The tool uses PyMuPDF to read the PDF and extract each page as a pixmap. The pixmap is then converted to a NumPy array and processed with OpenCV to save as a PNG image.

Each page is saved with the naming convention `page_N.png` where N is the page number (starting from 1).

## License

[MIT License](LICENSE) 