"""
This code reads each CSV file from the original ZIP file one by one,
and checks if it is larger than 100MB. If it is, it splits it into 
multiple smaller files, creates a new ZIP archive with the same name as the original.
"""
import os
import shutil
import zipfile
from tqdm import tqdm

# path to the original ZIP file
original_path = "data/ETLSINASC.zip"

# create a temporary directory to extract the files to
temp_dir = 'split'
os.makedirs(temp_dir, exist_ok=True)

# open the original ZIP file
with zipfile.ZipFile(original_path, 'r') as zip_file:

    # iterate over each file in the ZIP archive
    for zip_info in tqdm(zip_file.infolist()[97:]):

        # extract the file to the temporary directory
        zip_file.extract(zip_info, temp_dir)

        # get the full path to the extracted file
        file_path = os.path.join(temp_dir, zip_info.filename)

        # split the file into smaller chunks
        with open(file_path, 'rb') as f:
            chunk_size = 24 * 1024 * 1024  # 24MB in bytes
            chunk_num = 0
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                chunk_filename = f'{zip_info.filename[:-4]}_chunk{chunk_num:03}.csv'
                chunk_path = os.path.join(temp_dir, chunk_filename)
                with open(chunk_path, 'wb') as chunk_file:
                    chunk_file.write(chunk)
                chunk_num += 1

        # delete the extracted file
        os.remove(file_path)
