import glob
import os


def get_files_in_folder(extension, path):
    os.chdir(path)
    return glob.glob(f"*.{extension}")
