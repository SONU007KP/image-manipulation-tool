
# Image Manipulation Tool

A command-line image manipulation tool built using Python, NumPy, and Pillow. It allows users to select images from their computer, apply common image transformations through an interactive menu, and save the edited images as PNG files.

## Technologies Used

- **Python:** Implements the application logic and interactive menu.
- **NumPy:** Represents images as arrays and performs pixel-level operations.
- **Pillow:** Loads, displays, transforms, and saves images.
- **Tkinter:** Provides file-selection and Save As dialogs.
- **Command-line interface (CLI):** Allows users to interact with the program through the terminal.

## Features

- Select images from your computer using a file picker.
- Crop images using custom percentages for each side.
- Flip images horizontally and vertically.
- Rotate images by 90°, 180°, or 270°.
- Convert color images to grayscale.
- Adjust image brightness and darkness.
- Reset edits to restore the originally selected image.
- Save edited images as PNG files.
- Choose the destination folder and filename using a Save As dialog.
- Handle invalid menu choices, invalid numeric inputs, and common image-loading and saving errors.

## Requirements

- Python 3.11 or a compatible version.
- NumPy
- Pillow
- Tkinter (usually included with Python).

## Installation

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:

   ```bash
   python main.py
   ```

2. Select an image in the file-selection window.
3. Choose an operation from the terminal menu.
4. Use Reset to restore the original selected image if needed.
5. Choose Save to select the output filename and destination.

## Project Structure

```text
Image manipulation/
├── images/
├── output/
├── main.py
├── image_operations.py
├── requirements.txt
├── .gitignore
└── README.md
```