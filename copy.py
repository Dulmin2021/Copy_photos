import os
import shutil

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

if __name__ == "__main__":
    source_directory = input("Enter the source directory: ")
    destination_directory = input("Enter the destination directory: ")

    copy_photos(source_directory, destination_directory)
    print("All photos have been copied successfully.")
