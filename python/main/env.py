import os


def get_home_path() -> str:
    """
    home_path = get_home_path()
    home_path       # $REPO_PATH
    """
    return os.environ.get("COMMON_CODE_HOME")


def get_main_python_path() -> str:
    """
    home_path = get_home_path()
    home_path       # $REPO_PATH/python/main
    """
    return os.environ.get("COMMON_CODE")
