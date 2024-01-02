import os
import shutil

def copy_folders(src_path, dest_path):
    # Get a list of all folders in the source location
    folder_names = [folder for folder in os.listdir(src_path) if os.path.isdir(os.path.join(src_path, folder))]

    # Create corresponding folders in the destination location
    for folder_name in folder_names:
        src_folder_path = os.path.join(src_path, folder_name)
        dest_folder_path = os.path.join(dest_path, folder_name)

        # Create the folder in the destination location
        try:
            os.makedirs(dest_folder_path)
            print(f"Folder '{folder_name}' copied successfully.")
        except OSError as e:
            print(f"Failed to copy folder '{folder_name}': {e}")

if __name__ == "__main__":
    # Specify the source and destination paths
    source_location = ""
    destination_location = ""

    # Call the function to copy folders
    copy_folders(source_location, destination_location)
