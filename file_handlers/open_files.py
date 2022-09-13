def open_files(source_files):
    files = [open(filename) for filename in source_files]
    return files