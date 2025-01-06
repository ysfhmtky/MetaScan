# 📑 **MetaScan**

**MetaScan** is a Python-based tool that extracts metadata from PDF and image files. It provides an easy-to-use interface for examining file information such as document metadata and EXIF data in images. The tool supports the extraction of metadata from PDF files and EXIF metadata from image files (such as JPEGs and PNGs).

## 🚀 Features

- 📄 **PDF Metadata Extraction**: Extract metadata from PDF files (author, title, creation date, etc.).
- 🖼️ **Image EXIF Metadata Extraction**: Extract EXIF metadata from image files (camera settings, GPS coordinates, etc.).
- 🎨 **Stylish Banner**: Interactive banner display with a neon blue theme.
- 🔧 **User-friendly Interface**: Simple menu-based interface for easy navigation.

## 📝 Prerequisites

To run **MetaScan**, you'll need:

- Python 3.x
- `PyPDF2` library for PDF file handling.
- `exifread` library for reading EXIF data from image files.
- `pyfiglet` library for generating the stylish banner.

### Install Required Libraries

Run the following command to install the necessary Python libraries:

```bash
pip install PyPDF2 exifread pyfiglet
```
🔧 Usage

Clone this repository to your local machine:

```Copy code
git clone https://github.com/yourusername/MetaScan.git
cd MetaScan
```
Run the script:

```Copy code
python MetaScan.py
Select one of the available options:
Option 1: Extract PDF metadata by providing the PDF file path.
Option 2: Extract image metadata by providing the image file path.
Option 3: Exit the program.
```
Example Usage
Extract PDF Metadata

```Copy code
Enter your choice (1/2/3): 1
Enter the PDF file path: /path/to/yourfile.pdf
[INFO] PDF Metadata:
Title: Example PDF
Author: Mr.CodeX
CreationDate: D:20210101000000Z
...
Extract Image Metadata (EXIF)
plaintext
Copy code
Enter your choice (1/2/3): 2
Enter the image file path: /path/to/yourimage.jpg
[INFO] Image EXIF Metadata:
Image Width: 1920
Image Height: 1080
Make: Canon
Model: EOS 80D
GPS Latitude: 37.7749
GPS Longitude: -122.4194
```
📄 File Structure

```Copy code
MetaScan/
├── MetaScan.py      # Main Python script
└── README.md        # Project documentation
```
🤝 Contributing

If you'd like to contribute to MetaScan, follow these steps:

Fork the repository.
```
Create a new branch (git checkout -b feature-name).
Make your changes.
Commit your changes (git commit -am 'Add feature').
Push to the branch (git push origin feature-name).
Create a new Pull Request.
```
⚠️ Disclaimer
MetaScan is intended for educational and personal use. Please use it responsibly and respect the privacy of others when extracting metadata from files.

✨ Enjoy exploring file metadata with MetaScan! ✨


### Key Points in the README:
- Includes clear setup and usage instructions.
- Provides examples for extracting PDF and image metadata.
- Describes the file structure for clarity.
- Encourages responsible use with a **Disclaimer**.

Let me know if you need any adjustments! 🌟
