"""
Description: Tests for file io functions.
"""

import pytest

from file_io import (create_absolute_file_paths)


@pytest.mark.parametrize(
    "file_list,file_path,expected",
    [(["file1.csv",
       "file2.csv",
       "file3.csv"],
       "/dir1/",
      ["/dir1/file1.csv",
       "/dir1/file2.csv",
       "/dir1/file3.csv"]),
     (["file1.csv"], "/dir1/", "/dir1/file1.csv")])
def test_create_absolute_file_paths(
        file_list: list[str],
        file_path: str,
        expected: list[str]) -> list[str] | str:
    """
    Tests the following:
    1. Tests whether specified files were correctly joined with a
        corresponding absolute file path.

    Arguments:
        file_list (strList): List of files to join with a specified absolute
            path.
        file_path (str): The file path to join the files specified in
            'file_list' to.
        expected (StrList): The expected test case.

    Returns:
        NONE

    """
    test_file_paths = create_absolute_file_paths(
        file_list=file_list,
        file_path=file_path)

    assert test_file_paths == expected


@pytest.mark.parametrize(
    "file_list,file_path,expected",
    [("file1.csv", "/dir1/", "/dir1/file1.csv"),
     (["file1.csv"], ["/dir1/"], "/dir1/file1.csv")])
def test_create_absolute_file_paths_type_exceptions(
        file_list: list[str],
        file_path: str,
        expected: list[str]) -> list[str] | str:
    """
    Tests the following:
    1. Tests whether TypeErrors are raised if the value of variable
        'file_list' is not of type 'list'.
    2. Tests whether TypeErrors are raised if the value of variable
        'file_path' is not of type 'str'.

    Arguments:
        file_list (strList): List of files to join with a specified absolute
            path.
        file_path (str): The file path to join the files specified in
            'file_list' to.
        expected (StrList): The expected test case.

    Returns:
        NONE

    """
    with pytest.raises(TypeError):

        create_absolute_file_paths(
            file_list=file_list,
            file_path=file_path)
