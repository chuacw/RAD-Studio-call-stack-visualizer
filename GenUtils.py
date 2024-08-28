# GenUtils.py

def save_string_to_file(content: str, file_path: str) -> None:
    """
    Saves the given string content to a specified file path.

    :param content: The string content to save.
    :param file_path: The path of the file where the content will be saved.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

