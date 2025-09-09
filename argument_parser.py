import argparse


def create_parser():
    """Create and configure the argument parser for the CLI tool."""
    parser = argparse.ArgumentParser(
        prog="http",
        description="A CLI tool to query and manage HTTP status codes and descriptions.",
        epilog='Use "http help" for more information on a specific command.',
    )

    subparsers = parser.add_subparsers(
        dest="command", help="Available commands", required=False
    )

    # Command: http <code>
    get_parser = subparsers.add_parser(
        "get",
        help="Display the description for an HTTP status code.",
        description="Display the description for an HTTP status code.",
    )
    get_parser.add_argument("code", help="The HTTP status code (e.g., 200, 404)")

    # Command: http edit <code> <description>
    edit_parser = subparsers.add_parser(
        "edit",
        help="Edit the description for an HTTP status code.",
        description="Edit the description for an HTTP status code.",
    )
    edit_parser.add_argument("code", help="The HTTP status code (e.g., 200, 404)")
    edit_parser.add_argument(
        "description", help="The new description for the HTTP status code"
    )

    # Command: http reset <code>
    reset_parser = subparsers.add_parser(
        "reset",
        help="Reset the description for an HTTP status code to its original value.",
        description="Reset the description for an HTTP status code to its original value.",
    )
    reset_parser.add_argument(
        "code", nargs="?", help="The HTTP status code to reset (e.g., 200, 404)"
    )
    reset_parser.add_argument(
        "--all",
        action="store_true",
        help="Reset all custom descriptions to their original values",
    )
    reset_parser.add_argument(
        "--yes",
        "-y",
        action="store_true",
        help="Skip confirmation prompt when resetting all descriptions",
    )

    # Command: http help
    help_parser = subparsers.add_parser(
        "help",
        help="Display help information.",
        description="Display help information.",
    )

    # Handle positional argument for direct code lookup (http <code>)
    parser.add_argument(
        "positional_code",
        nargs="?",
        help="The HTTP status code to look up (e.g., 200, 404)",
    )

    return parser


def parse_arguments(args):
    """Parse the command-line arguments.

    Args:
        args: The command-line arguments to parse.

    Returns:
        tuple: A tuple containing (command, command_args).
    """
    parser = create_parser()

    # Check if the first argument is a 3-digit number (HTTP status code)
    if args and len(args) > 0 and args[0].isdigit() and len(args[0]) == 3:
        return "get", {"code": args[0]}

    parsed_args = parser.parse_args(args)

    # Handle direct code lookup (http <code>)
    if parsed_args.command is None and parsed_args.positional_code:
        return "get", {"code": parsed_args.positional_code}

    # Handle default help command
    if parsed_args.command is None:
        return "help", {}

    # Convert parsed args to a dictionary
    command_args = vars(parsed_args)
    command = command_args.pop("command")

    # Special handling for reset command
    if command == "reset":
        if parsed_args.all:
            # If --all is specified, we don't need the code argument
            command_args.pop("code", None)
        elif not parsed_args.code:
            # If neither --all nor code is specified, show help for reset
            return "help", {"command": "reset"}

    return command, command_args
