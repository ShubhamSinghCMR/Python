   


def get_long_description(path):
    """
    Get long description from file.
    """
    if path:
        with open(path, "rt") as fp:
            return fp.read()
    return None
