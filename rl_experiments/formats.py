"""Definitions about format, and related functionalities."""

from pathlib import Path

import yaml

# All format files
defs_path = Path(__file__).parent / "defs"
format_files = {f.name: f for f in defs_path.iterdir() if f.suffix == ".yaml"}


def compose(format_name: str) -> dict:
    """Compose this format file with all nested subformats."""
    # Read
    with open(format_files[format_name], "r") as f:
        data = yaml.safe_load(f)

    return _compose(data)


def _compose(obj):
    """Compose format recursively, auxiliary function."""
    # Stop recursion
    if not isinstance(obj, (dict, list)):
        # Substitute if necessary
        if obj in format_files:
            return compose(obj)
        else:
            return obj

    # Is this a list
    if isinstance(obj, list):
        return [_compose(o) for o in obj]

    # Is this a dict
    if isinstance(obj, dict):
        return {k: _compose(v) for k, v in obj.items()}


def print_format(format_name, merge=False):
    """Print a format file."""
    # Print as it is
    if not merge:
        file_path = format_files[format_name]
        with open(file_path, "r") as f:
            print(f.read())

    # Parse and print
    else:
        data = compose(format_name)
        filestr = yaml.dump(data)
        print(filestr)
