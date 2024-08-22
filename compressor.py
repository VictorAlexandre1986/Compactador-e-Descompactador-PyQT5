import zipfile
import os

def compress_files(files, output_zip):
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))

def decompress_file(zip_file, output_dir):
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        zipf.extractall(output_dir)
