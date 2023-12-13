"""
Description: Functions for handeling processing related to input and output
files.
"""

import logging

def create_absolute_file_paths(
        file_list: list[str],
        file_path: str) -> list[str] | str:
    """

    Arguments:
        file_list (strList): List of files to join with a specified absolute
            path.
        file_path (str): The file path to join the files specified in
        'file_list' to.

    Returns:
        Either a list of absolute file paths or a single absolute file
        path depending on the length of file_list.

    Raises:
        TypeError if the value of the 'file_list' argument  is not a list.
        TypeError if the value of the 'file_path' is not a string.
        TypeError if elements of 'file_list' are not strings.
        ValueError if elements of 'file_list' do not contain file extensions.
        ValueError if the value of the 'file_path' does not begin with a '/'.
        ValueError if elements of file_name do not contain characters before
            the '.' of the file extension (e.g. '.csv')
    """

    # Confirm values for 'file_list' are not strings and 'file_path' are not
    # lists.
    if type(file_list) is not list:
        raise TypeError("The value of 'file_list' should be a list")
    if type(file_path) is not str:
        raise TypeError("The value of 'file_path' should be a string")
    if file_path[0] != '/':
        raise ValueError("The value of 'file_path' must start with a '/'")

    abs_file_paths = []

    for file_name in file_list:
        print(file_name)
        if type(file_name) is not str:
            raise TypeError("Elements of 'file_list' should be of type str")
        if '.' not in file_name:
            raise ValueError(
                f'File name {file_name} is missing file extension')
        if file_name[0] == '.':
            raise ValueError(
                f'File name {file_name} only contains the file extension and '
                f'is missing an actual file name.')

        logging.info(
            f'Joining file path {file_path} with file {file_name}')
        abs_path = f'{file_path}{file_name}'
        abs_file_paths.append(abs_path)

    # Return either a list of file paths or a single file path.
    if len(abs_file_paths) > 1:
        return abs_file_paths
    else:
        return abs_file_paths[0]
