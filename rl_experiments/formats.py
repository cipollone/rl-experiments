"""Definitions about format, and related functionalities."""

from pathlib import Path

import yaml

# All format files
defs_path = Path(__file__).parent / "defs"
format_files = {f.name: f for f in defs_path.iterdir() if f.suffix == ".yaml"}


def compose(format_name: str) -> dict:
    """Compose this format file with all subfiles together.

    Note: this assumes that nesting only happens at top-level.
    """
    # Names without extension
    format_names = {f.stem: f.name for f in format_files.values()}
    assert format_name in format_files

    # Read
    with open(format_files[format_name], "r") as f:
        data = yaml.safe_load(f)

    # Add if name is equal
    for k, v in data.items():
        if k in format_names:
            assert isinstance(v, dict)

            # Load sub
            data[k] = compose(format_names[k])

    return data


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
