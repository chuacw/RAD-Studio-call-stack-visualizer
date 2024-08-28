import os

def change_file_ext(filename: str, ext: str) -> str:
    """
    Renames the file extension of the given filename to ext.

    :param filename: The original filename.
    :return: The filename with the new ext extension.
    """
    base, _ = os.path.splitext(filename)
    if not ext.startswith('.'):
        ext = '.' + ext
    return f"{base}{ext}"