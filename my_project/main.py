import os
import shutil
import argparse
from pathlib import Path

def parse_arguments():
    parser = argparse.ArgumentParser(description="Copy files from source to destination, sorted by file extension.")
    parser.add_argument('source', type=str, help="Path to the source directory.")
    parser.add_argument('destination', type=str, nargs='?', default='dist', help="Path to the destination directory (default: dist).")
    return parser.parse_args()

def copy_files_recursively(source_dir, dest_dir):
    try:
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            if os.path.isdir(source_path):
                copy_files_recursively(source_path, dest_dir)
            elif os.path.isfile(source_path):
                file_extension = Path(source_path).suffix[1:]  # отримуємо розширення файлу без крапки
                if file_extension:
                    target_dir = os.path.join(dest_dir, file_extension)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.copy2(source_path, target_dir)
                else:
                    target_dir = os.path.join(dest_dir, 'no_extension')
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.copy2(source_path, target_dir)
    except Exception as e:
        print(f"Error: {e}")

def main():
    args = parse_arguments()
    source_dir = args.source
    dest_dir = args.destination

    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    copy_files_recursively(source_dir, dest_dir)
    print(f"Files copied successfully from '{source_dir}' to '{dest_dir}' and sorted by file extension.")

if __name__ == "__main__":
    main()
