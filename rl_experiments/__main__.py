"Main script: entry point"

import argparse

from . import formats, train


def main():
    """Main function."""
    # Args
    parser = argparse.ArgumentParser(
        description="Simple protocols for running RL experiments")
    subparsers = parser.add_subparsers(dest="op", help="What to do")

    format_parser = subparsers.add_parser(
        "show-format",
        help="show a format file",
    )
    format_parser.add_argument(
        "file",
        choices=formats.format_files.keys(),
    )
    format_parser.add_argument(
        "--comment",
        action="store_true",
        help="Print a single file, not nested components, with comments.",
    )

    train_parser = subparsers.add_parser(
        "train",
        help="Executes an experiment (training)",
    )
    train_parser.add_argument(
        "-e",
        "--experiment",
        type=str,
        required=True,
        help="an experiment.yaml file"
    )

    args = parser.parse_args()

    # Do
    if args.op == "show-format":
        formats.print_format(args.file, merge=not args.comment)
    if args.op == "train":
        train.start(args.experiment)


if __name__ == "__main__":
    main()
