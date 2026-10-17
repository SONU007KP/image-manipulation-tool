import numpy as np
from PIL import Image
from image_operations import crop, flip_horizontal, flip_vertical, rotate, grayscale, brightness
from pathlib import Path
from tkinter import Tk, filedialog

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)


root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select an image to edit",
    filetypes=[
        ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.tif *.webp"),
        ("All files", "*.*")
    ]
)

root.destroy()

if not image_path:
    print("No image selected. Goodbye!")
    raise SystemExit

try:
    with Image.open(image_path) as im:
        image_array = np.array(im.convert("RGB"))

except (OSError, ValueError) as error:
    print(f"Could not open image: {error}")
    raise SystemExit

original_image_array = image_array.copy()


while True:
    try:
        choice = int(input("""
            IMAGE MANIPULATION TOOL

            1. Crop
            2. Flip horizontally
            3. Flip vertically
            4. Rotate
            5. Grayscale
            6. Brightness
            7. Save
            8. Reset image
            9. Exit

            Enter your choice: 
        """))


        if choice == 1:
            try:
                top = float(input("Crop from top (%): "))
                bottom = float(input("Crop from bottom (%): "))
                left = float(input("Crop from left (%): "))
                right = float(input("Crop from right (%): "))

                if any(value < 0 or value > 100 for value in
                    (top, bottom, left, right)):
                    print("Percentages must be between 0 and 100.")
                    continue

                if top + bottom >= 100 or left + right >= 100:
                    print("Crop amounts are too large. Try smaller values.")
                    continue

                image_array = crop(image_array, top, bottom, left, right)
                Image.fromarray(image_array).show()

            except ValueError:
                print("Please enter valid numbers.")


        elif choice == 2:
            image_array = flip_horizontal(image_array)
            Image.fromarray(image_array).show()


        elif choice == 3:
            image_array = flip_vertical(image_array)
            Image.fromarray(image_array).show()

        elif choice == 4:
            while True:
                try:    
                    k = int(input("""
                                    Enter rotation:
                                        1. 90° counterclockwise
                                        2. 180°
                                        3. 270° counterclockwise (90° clockwise)
                                    """))

                    if k not in (1, 2, 3):
                        print("Invalid choice")
                        continue
                    
                    image_array = rotate(image_array, k)
                    Image.fromarray(image_array).show()

                    break

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == 5:
            image_array = grayscale(image_array)
            Image.fromarray(image_array).show()

        elif choice == 6:
            try:
                value = int(input("Enter brightness value (-255 to 255): "))
                if value < -255 or value > 255:
                    print("Please enter a value between -255 and 255.")
                    continue

                image_array = brightness(image_array, value)
                Image.fromarray(image_array).show()

            except ValueError:
                print("Please enter a valid number.")

        
        elif choice == 7:
            root = Tk()
            root.withdraw()

            output_path = filedialog.asksaveasfilename(
                title="Save edited image",
                initialdir=str(output_dir.resolve()),
                defaultextension=".png",
                filetypes=[("PNG images", "*.png")]
            )

            root.destroy()

            if not output_path:
                print("Save cancelled.")
                continue

            if Path(output_path).resolve() == Path(image_path).resolve():
                print("Cannot overwrite the original image. Choose a different path.")
                continue

            try:
                Image.fromarray(image_array).save(output_path, format="PNG")
                print(f"Image saved as {output_path}")
            except (OSError, ValueError) as error:
                print(f"Could not save image: {error}")
   
        
        elif choice == 8:
            image_array = original_image_array.copy()
            print("Image reset to its original state.")
            Image.fromarray(image_array).show()

        elif choice == 9:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")
    
    except ValueError:
        print("Invalid choice")
        continue