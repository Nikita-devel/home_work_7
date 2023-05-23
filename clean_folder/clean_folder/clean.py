import os
import shutil


def clean_folder(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    clean_folder(folder_path)
