from PIL import Image
import os
from clc99 import *  
import keyboard
import msvcrt
import sys

def crop_image(image_path):
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')
    if not image_path.lower().endswith(valid_extensions):
        print_error(f"{os.path.basename(image_path)} is not a valid image file!")
        return False

    try:
        with Image.open(image_path) as img:
            img_width, img_height = img.size
            print_status(f"Original image size: Width={img_width}, Height={img_height}")
            
            # Crop coordinates for VRChat instant photo (adjusted for white border removal)
            left = 65
            upper = 70
            right = 1980
            lower = 1149
            
            if right > img_width or lower > img_height:
                print_warning(f"Crop coordinates exceed image boundaries!")
                print_status(f"Crop area dimensions: Width={right-left}, Height={lower-upper}")
                print_status(f"Please check image size or adjust crop coordinates")
                return
            
            cropped_img = img.crop((left, upper, right, lower))
            
            # Generate output filename with "_cropped" suffix
            filename = os.path.splitext(image_path)[0] + "_cropped" + os.path.splitext(image_path)[1]
            output_path = os.path.join(os.getcwd(), filename)
            
            # Overwrite confirmation
            if os.path.exists(output_path):
                print_warning(f"{filename} already exists in the current directory. Overwrite? (Press Y to continue, N to skip)")
                while True:
                    if keyboard.is_pressed('y'):
                        break
                    elif keyboard.is_pressed('n'):
                        print_status(f"Skipping save for {filename}")
                        return
            
            cropped_img.save(output_path)
            print_good(f"Crop completed! File saved to: {output_path}")
            print_status(f"Cropped image size: Width={cropped_img.width}, Height={cropped_img.height}")
            
    except FileNotFoundError:
        print_error(f"File {image_path} not found. Please check the path is correct")
    except PermissionError:
        print_error(f"Permission denied to access {image_path} or save output file")
    except Exception as e:
        print_error(f"Error processing image: {str(e)}")

if __name__ == "__main__":
    # ASCII art logo for 99VRCPhotoCut
    ascii_art = r"""


  ___   _____     ______  ____  _           _         ____      _   
 / _ \ / _ \ \   / /  _ \|  _ \| |__   ___ | |_ ___  / ___|   _| |_
| (_) | (_) \ \ / /| |_) | |_) | '_ \ / _ \| __/ _ \| |  | | | | __|
 \__, |\__, |\ V / |  _ <|  __/| | | | (_) | || (_) | |__| |_| | |_
   /_/   /_/  \_/  |_| \_\_|   |_| |_|\___/ \__\___/ \____\__,_|\__|

   

"""
    print(ascii_art)
    print_notrun("Welcome to 99VRChat Instant Photo Cropper!")

    # Check if no files are dragged in
    if len(sys.argv) < 2:
        print_error("Please drag image files directly onto this script icon!")
        print_status("Press any key to exit...")
        msvcrt.getch()
        sys.exit(1)
    else:
        success_count = 0
        total_count = len(sys.argv) - 1

    print_status(f"Detected {total_count} files. Processing...")

    # Process all dragged files
    for f in sys.argv[1:]:
        if os.path.isfile(f):
            print_status(f"Processing image: {f}")
            if crop_image(f):  # Fix: Only count successful crops
                success_count += 1
        else:
            print_warning(f"Skipping non-file item: {f}")

    print_good(f"Processing complete! Successfully cropped {success_count} images.")
    print_status("Press any key to exit...")
    msvcrt.getch()