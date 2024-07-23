import os
import shutil
from pyimobiledevice import idevice, idevicephoto

def copy_photos(source_dir, dest_dir, extensions=None):
    if extensions is None:
        extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)

    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                source_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)
                
                # Copy the file
                shutil.copy2(source_file, dest_file)
                print(f"Copied {source_file} to {dest_file}")

def export_iphone_photos(dest_dir):
    # Connect to the iPhone
    phone = idevice.Idevice()
    
    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)

    # Export photos from iPhone to the destination directory
    photos = idevicephoto.IdevicePhoto(phone)
    for photo in photos.list_photos():
        photo_data = photos.get_photo(photo)
        dest_file = os.path.join(dest_dir, photo)
        with open(dest_file, 'wb') as f:
            f.write(photo_data)
        print(f"Copied iPhone photo to {dest_file}")

if __name__ == "__main__":
    # Prompt user for source and destination directories for manual photo copying
    source_directory = input("Enter the source directory (leave blank to skip): ")
    destination_directory = os.path.join(os.path.expanduser("~"), "Documents", "Exported_Photos")
    
    if source_directory:
        copy_photos(source_directory, destination_directory)
    
    # Export photos from iPhone if connected
    try:
        export_iphone_photos(destination_directory)
        print("All iPhone photos have been copied successfully.")
    except Exception as e:
        print(f"Could not copy iPhone photos: {e}")

    print("All photos have been copied successfully.")
