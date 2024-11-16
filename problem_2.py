import os

def find_files(suffix: str, path: str) -> list[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Parameters:
    -----------
    suffix : str
        The suffix of the files to be found.
    path : str
        The root directory path where the search should begin.

    Returns:
    --------
    list[str]
        A list of file paths that end with the given suffix.
    """
    result = []

    # Check if the provided path is a directory
    if not os.path.isdir(path):
        return result

    # List all items in the directory
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)

        # If entry is a directory, recursively search inside it
        if os.path.isdir(entry_path):
            result.extend(find_files(suffix, entry_path))
        
        # If entry is a file and ends with the specified suffix, add to result
        elif os.path.isfile(entry_path) and entry.endswith(suffix):
            result.append(entry_path)

    return result

if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    print("Test Case 1: Standard directory structure")
    result = find_files(".c", "./testdir")
    print(result)
    # Expected output: ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

    # Test Case 2: Search for .py files in an empty directory
    print("Test Case 2: Empty directory for .py files")
    result = find_files(".py", "./emptydir")
    print(result)
    # Expected output: []

    # Test Case 3: Directory with no matching files
    print("Test Case 3: Search with no matching files")
    result = find_files(".java", "./testdir")
    print(result)
    # Expected output: []
