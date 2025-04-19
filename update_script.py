import os
import shutil
import zipfile
import urllib.request
import time

# URL to the ZIP file with the updated app
ZIP_URL = "https://github.com/bboB-Bobb/Simple-Macro/releases/download/Software/MacroRAR.zip"

def download_and_replace():
    zip_path = "update.zip"
    extract_path = "update_temp"

    print("Downloading update...")
    urllib.request.urlretrieve(ZIP_URL, zip_path)

    print("Extracting update...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    # Locate the new folder inside the zip (assuming one folder inside root)
    new_folder_path = os.path.join(extract_path, os.listdir(extract_path)[0])

    print("Replacing existing files...")
    for item in os.listdir(new_folder_path):
        src = os.path.join(new_folder_path, item)
        dest = os.path.join(os.getcwd(), item)

        if os.path.exists(dest):
            if os.path.isdir(dest):
                shutil.rmtree(dest)
            else:
                os.remove(dest)

        if os.path.isdir(src):
            shutil.copytree(src, dest)
        else:
            shutil.copy2(src, dest)

    print("Cleaning up...")
    os.remove(zip_path)
    shutil.rmtree(extract_path)

    print("Update complete. Please restart the application.")

if __name__ == "__main__":
    download_and_replace()
    print("Update complete. This script will now delete itself.")
    time.sleep(1)
    os.remove(__file__)
