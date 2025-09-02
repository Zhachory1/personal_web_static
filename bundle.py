import os
import glob
import shutil

FROM_DIR="src"
TO_DIR="public"

FILES=[
  "*.html",
  "favicon.ico",
  "sitemap.xml",
  "css/*.css",
  "js/*.min.js",  # javascript files are REQUIRED to be minified
  "libs/**/*",
  "images/*",  # We expect a flat directory of images
  "ZhachResume_20250612.pdf",  # The main star! I need me resume here
]

if __name__ == "__main__":
  # clear the destination folder
  shutil.rmtree(TO_DIR)
  os.makedirs(TO_DIR, exist_ok=True)
  for pattern in FILES:
    source_path = os.path.join(FROM_DIR, pattern)
    
    # Expand the glob pattern to get a list of files/directories
    files = glob.glob(source_path, recursive=True)
    
    for file in files:
      dest_path = os.path.join(TO_DIR, os.path.relpath(file, FROM_DIR))

      if os.path.isfile(file):
        # Ensure the destination directory exists
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.copy2(file, dest_path)  # copy with metadata
        print(f"Copied file: {file} to {dest_path}")
      elif os.path.isdir(file):
        # Ensure the destination directory exists
        os.makedirs(dest_path, exist_ok=True)
        # Use copytree to copy the directory structure and files
        shutil.copytree(file, dest_path, dirs_exist_ok=True)
        print(f"Copied directory: {file} to {dest_path}")