# Text to PDF Converter 📝→📄

A Python script that automatically converts multiple text files into a single, well-formatted PDF document. Perfect for creating consolidated reports or documentation from individual text files.

## Features ✨

- **Batch Processing**: Converts all `.txt` files in a directory at once
- **Automatic Formatting**:
  - Adds title from filename (converted to Title Case)
  - Clean typography with Times font
  - Proper paragraph spacing
- **Customizable Output**:
  - Adjustable page size (A4 by default)
  - Configurable font styles and sizes
- **Simple Integration**: Easy to add to existing workflows

## Input Structure
    Text_Files/
    ├── cats.txt
    ├── dogs.txt
    ├── foxes.txt
    └── snakes.txt

## Sample Output PDF
1. Cats
[Content from cats.txt]

2. Dogs  
[Content from dogs.txt]

3. Foxes  
[Content from foxes.txt]

4. Snakes  
[Content from snakes.txt]

## Setup & Usage 🚀

### 1. Install Requirements
```
pip install fpdf2
```
### 2. Run Conversion
```
python text_to_pdf.py
```

## Get Output
The script will generate:
text_to_pdf.pdf in your project root

Each text file becomes a new section with:

Filename as title (e.g., "Cats" from cats.txt)

Content formatted with clean typography